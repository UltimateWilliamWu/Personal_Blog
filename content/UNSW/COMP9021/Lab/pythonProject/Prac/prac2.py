def positive_gaps(L):
    # if not L:
    #     print("Empty list.")
    #     return
    # else:
    #     gaps = {}
    #     for index in range(len(L) - 1):
    #         a = L[index]
    #         b = L[index + 1]
    #         if b > a:
    #             gap = abs(b - a)
    #             if gap not in gaps:
    #                 gaps[gap] = []
    #             if (a, b) not in gaps[gap]:  # 防止重复
    #                 gaps[gap].append((a, b))
    #
    #     if not gaps:
    #         print("No positive gaps.")
    #         return
    #
    #     for gap in sorted(gaps):
    #         print(f"Gaps of {gap}:")
    #         for start, end in sorted(gaps[gap]):
    #             print(f"  Between {start} and {end}")
    if not L:
        return None
    else:
        gaps = {}
        for index in range(len(L) - 1):
            gap = abs(L[index + 1] - L[index])
            if L[index + 1] > L[index]:
                gaps[gap] = []
                gaps[gap].append((index, index + 1))
        for gap in sorted(gaps):
            print(f"Gaps of {gap}")
            for start, end in sorted(gaps[gap]):
                print(f"  Between {start} and {end}")


positive_gaps([1, 3, 3, 0, 3, 0, 3, 7, 5, 0, 3, 6, 3, 1, 4])
