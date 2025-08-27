import matplotlib.pyplot as plt
import pandas as pd
import os
import sys


def plot_hidden_states(csv_path, save_path=None):
    df = pd.read_csv(csv_path)

    if 'input' not in df.columns:
        print("❌ CSV 中缺少 'input' 列。")
        return

    # 生成横坐标索引
    x = list(range(len(df)))
    tokens = df['input'].tolist()
    hidden_cols = [col for col in df.columns if col.startswith('h')]
    hidden_dim = len(hidden_cols)

    plt.figure(figsize=(max(10, len(tokens) * 0.6), 6))
    for col in hidden_cols:
        values = df[col].values
        plt.plot(x, values, label=col, linewidth=1.5)

    plt.xticks(ticks=x, labels=tokens, rotation=45, fontsize=10)
    plt.xlabel("Input Token", fontsize=14)
    plt.ylabel("Hidden State Value", fontsize=14)
    plt.title(f"Hidden State Dynamics ({os.path.basename(csv_path)})", fontsize=16)
    plt.legend(loc='upper right', fontsize=8, ncol=2)
    plt.grid(True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300)
        print(f"[✓] 图像已保存：{save_path}")
    else:
        plt.show()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python plot_hidden.py <csv文件路径> [保存图像路径]")
        sys.exit(1)

    csv_file = sys.argv[1]
    save_file = sys.argv[2] if len(sys.argv) >= 3 else None

    plot_hidden_states(csv_file, save_file)
