## Python Basic Programming
```Python
23 ** 3=pow(23,3) #python表示次方
L = ['COMP9021', 'Thursday', 2025]
L[-1]=2025 #从末尾开始遍历列表
tape = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]
[1, 3] * 4 =[1, 3, 1, 3, 1, 3, 1, 3] #列表相乘相加都可以理解为类似于字符串的拼接
def display_tape():
    # Display top boundary 
    # Display tape contents, with | as separators
    # Display bottom boundary
    pass #使用pass定义空函数 return 表示返回为空
x=023 #语法 错误 不支持
x=0x23 #十六进制
x=0o23 #八进制
int('023')=23 #支持
[str(e) for e in tape] # 前面参数代表要执行的操作 如赋值 转变类型 后面for 代表列表循环
[x for x in nums if x!=val]
'ABC'.join([str(e) for e in tape]) #意味着使用'ABC'作为连接符
with open('division_by_2.txt') as file:
    file
    file.readlines() #一次性读取整个文本文件
    file.readline() #每次读取一行
    next(file) #读取一行同readline 适用于迭代器跳过某一行
    for line in file: #逐行读取文件
        print(line) #注意这里会在每一行末尾多加\n 输出和原本文件不同
    for line in file:
        print(line, end='') #去除\n 输出和原本文件一致
'ABCD'.startswith('') #判断前缀
'del1 1 del2 0 R'.split() #默认空格为分隔符 多个空格也算作一个空格
```

