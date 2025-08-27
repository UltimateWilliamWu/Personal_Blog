def triangle_characters(n):
    rows = n
    cols = 2 * n - 1
    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

    current_char_code = ord('A')

    for i in range(n):
        # 计算每一行中字符的起始位置
        start = n - 1 - i

        # 构造该行字符：正向 + 反向（去掉中间重复）
        forward = []
        for _ in range(i + 1):
            forward.append(chr(current_char_code))
            current_char_code += 1
            if current_char_code > ord('Z'):
                current_char_code = ord('A')
        backward = forward[:-1][::-1]
        full_chars = forward + backward

        # 填入矩阵
        for j, c in enumerate(full_chars):
            matrix[i][start + j] = c

    return matrix


if __name__ == '__main__':
    input_num = int(input("Enter a strictly positive integer: "))
    mat = triangle_characters(input_num)
    for row in mat:
        print(''.join(row))
