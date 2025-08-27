def f3(L):
    if not L:
        print([])
    else:
        remove_list = []
        last = L[-1]
        for i in reversed(L[:-1]):
            if i < last:
                remove_list.append(i)
            else:
                break
        result = [i for i in L if i not in remove_list]
        print(result)


f3([3, 2, 1, 0, 1, 2, 3])
