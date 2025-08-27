"""
   seq_train.py
   COMP9444, CSE, UNSW
"""

import argparse
import sys
import torch
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from seq_models import SRN_model, LSTM_model
from anb2n import lang_anb2n
import os
import csv

parser = argparse.ArgumentParser()
# language options
parser.add_argument('--lang', type=str, default='anb2n', help='anb2n or anb2nc3n')
parser.add_argument('--length', type=int, default=0, help='max number of As')
# network options
parser.add_argument('--model', type=str, default='srn', help='srn or lstm')
parser.add_argument('--hid', type=int, default=0, help='number of hidden units')
# optimizer options
parser.add_argument('--optim', type=str, default='sgd', help='sgd or adam')
parser.add_argument('--lr', type=float, default=0.005, help='learning rate')
parser.add_argument('--mom', type=float, default=0, help='momentum (srn)')
parser.add_argument('--init', type=float, default=0.001, help='initial weight size (srn)')
# training options
parser.add_argument('--epoch', type=int, default=0, help='number of training epochs (\'000s)')
parser.add_argument('--out_path', type=str, default='net', help='outputs path')
args = parser.parse_args()

if args.lang == 'anb2n':
    num_class = 2
    hid_default = 2
    epoch_default = 100
elif args.lang == 'anb2nc3n':
    num_class = 3
    if args.model == 'lstm':
        hid_default = 3
        epoch_default = 100
    else:  # srn
        hid_default = 4
        epoch_default = 200

if args.length == 0:
    args.length = 4

lang = lang_anb2n(num_class, args.length)

if args.hid == 0:
    args.hid = hid_default

if args.epoch == 0:
    args.epoch = epoch_default

if args.model == 'srn':
    net = SRN_model(num_class, args.hid, num_class)
    for m in list(net.parameters()):
        m.data.normal_(0, args.init)
elif args.model == 'lstm':
    net = LSTM_model(num_class, args.hid, num_class)

if args.optim == 'adam':
    optimizer = optim.Adam(net.parameters(), lr=args.lr,
                           weight_decay=0.0001)
else:
    optimizer = optim.SGD(net.parameters(), lr=args.lr,
                          momentum=args.mom, weight_decay=0.0001)

loss_function = F.nll_loss

np.set_printoptions(suppress=True, precision=2, sign=' ')


# ========== 添加函数：保存隐藏状态到 CSV ==========
def decode_token(index):
    if index == 0:
        return 'a'
    elif index == 1:
        return 'b'
    elif index == 2:
        return 'c'
    else:
        return '?'


def save_hidden_states(epoch, seq_tensor, hidden_tensor, out_dir='hidden_logs'):
    os.makedirs(out_dir, exist_ok=True)
    filename = f'{out_dir}/hidden_epoch{epoch}.csv'

    # 🟡 检查 hidden_tensor 是 LSTM 返回的 (h, c) 还是 SRN 的单个 tensor
    if isinstance(hidden_tensor, tuple):  # LSTM 返回 (h, c)
        hidden_tensor = hidden_tensor[0]  # 只取 hidden state
    hidden_tensor = hidden_tensor.detach().cpu()

    # 🟡 如果是 batch_first=False 且 shape 为 [1, seq_len, hidden], 则 squeeze batch 维
    if hidden_tensor.dim() == 3 and hidden_tensor.shape[0] == 1:
        hidden_tensor = hidden_tensor.squeeze(0)  # [seq_len, hidden]

    hidden_np = hidden_tensor.numpy()  # shape: [seq_len, hidden_dim]
    seq_np = seq_tensor.squeeze().detach().cpu().numpy()  # shape: [seq_len]

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        header = ['step', 'input'] + [f'h{i}' for i in range(hidden_np.shape[1])]
        writer.writerow(header)
        for t in range(hidden_np.shape[0]):
            token = decode_token(seq_np[t])
            row = [t, token] + [float(x) for x in hidden_np[t]]  # ✅ 强制转 float 避免 numpy 类型
            writer.writerow(row)


# ========== 主训练循环 ==========

for epoch in range((args.epoch * 1000) + 1):
    net.zero_grad()

    input, seq, target, state = lang.get_sequence()
    label = seq[1:]

    net.init_hidden()
    hidden, output = net(input)
    log_prob = F.log_softmax(output, dim=2)
    prob_out = torch.exp(log_prob)
    # loss = F.nll_loss(log_prob.squeeze(), label.squeeze())
    loss = F.nll_loss(log_prob.squeeze(), label.squeeze().long())
    loss.backward()
    optimizer.step()

    if epoch % 1000 == 0:

        # Check accuracy during training
        with torch.no_grad():
            net.eval()

            input, seq, target, state = lang.get_sequence()
            label = seq[1:]

            net.init_hidden()
            hidden, output = net(input)
            log_prob = F.log_softmax(output, dim=2)
            prob_out = torch.exp(log_prob)

            lang.print_outputs(epoch, seq, state, hidden, target, output)
            # 保存 hidden state 到文件（仅 LSTM 模型）
            if args.model == 'lstm' and epoch % 10000 == 0:
                save_hidden_states(epoch, seq.squeeze(), hidden)

            sys.stdout.flush()

            net.train()

        if epoch % 10000 == 0:
            path = args.out_path + '/'
            # torch.save(net.state_dict(),path+'%s_%s%d_%d.pth'
            #            %(args.lang,args.model,args.hid,epoch/1000))
            torch.save(net.state_dict(), f'{path}{args.lang}_{args.model}{args.hid}_{epoch // 1000}.pth')
