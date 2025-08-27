def f1(m, n):
    if m == 0:
        return ""
    if n == 0:
        return "||"

    result = ""
    for i in range(m):
        result += "|" + "_" * n + "|"
    result += "\n"

    return result


if __name__ == '__main__':
    print(f1(1, 0))
