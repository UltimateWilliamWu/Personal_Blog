# Written by *** for COMP9021
#
# Defines a function meant to take two integers x and y
# at least equal to 0 and having the same number of digits as arguments;
# x and y are to be read as the x and y coordinates of points, respectively.
# For instance, if x is 3040 and y is 2121, then the points are
# (3, 2), (0, 1) and (4, 2) (the point (0, 1) is duplicated).
# Consider that x coordinates increase from left to right
# and y coordinates increase from bottom to top.
#
# The function prints out the list of points in the order they are found
# by scanning the plane row by row, from top to bottom,
# and for a given row from left to right.
#
# The function displays the points as stars,
# with no trailing space on any line,
# except for the "origin", displayed as o,
# defining the "origin" as the leftmost lowest point.
#
# Finally, the function prints out the slopes of the lines
# that go through the "origin" and any other point,
# ordered from smallest to largest.
# When the line is horizontal, the slope is 0/1.
# When the line is vertical, the slope is inf/1
# (note that Python offers float('inf')).
# Consecutive slopes are separated by a comma and a space.
# When there is no slope, an empty line is output.


from math import gcd


def slopes(x, y):
    result = []
    # Adding tuple of list
    while x != 0 and y != 0:
        figure_x = x % 10
        figure_y = y % 10
        x = x // 10
        y = y // 10
        tuple_compare = (figure_x, figure_y)
        if tuple_compare not in result:
            result.append(tuple_compare)
    # Sorting the tuple
    n = len(result)
    # Bubble Sort
    for i in range(n - 1):
        for j in range(n - 1 - i):
            a = result[j]
            b = result[j + 1]

            # Descending sort of the second elements of tuple
            if a[1] < b[1]:
                # 交换
                result[j], result[j + 1] = result[j + 1], result[j]

            # Ascending sort of the first elements when they have the same second elements
            elif a[1] == b[1] and a[0] > b[0]:
                result[j], result[j + 1] = result[j + 1], result[j]

    print("Here is the list of points:")
    print(result)
    print("\nHere they are on the plane:")
    first_elements = [tup[0] for tup in result]
    second_elements = {}
    for tup in result:
        key = tup[1]
        if key in second_elements:
            second_elements[key].append(tup)  # Append to the existing list if key already exists
        else:
            second_elements[key] = [tup]  # Create a new list for the first appearance of the key

    first_max = max(first_elements)
    first_min = min(first_elements)

    second_max = max(second_elements)
    second_min = min(second_elements)
    origin = ()
    slope = set()
    for i in range(second_max, second_min - 1, -1):
        line_length = (first_max - first_min + 1) * 2
        line_list = [" "] * line_length

        if i in second_elements:
            for j in second_elements[i]:
                x_index = j[0] - first_min
                pos = x_index * 2

                if 0 <= pos < len(line_list):
                    line_list[pos] = "*"

            if i == second_min:
                # Find the minimum j[0]
                min_x = min([j[0] for j in second_elements[i]])
                for j in second_elements[i]:
                    if j[0] == min_x:
                        origin = j
                        break
                min_x_index = min_x - first_min
                min_pos = min_x_index * 2

                if 0 <= min_pos < len(line_list):
                    line_list[min_pos] = "o"

            print(f"{i} {''.join(line_list).rstrip()}")

        else:
            print(str(i))

    print("  " + " ".join(str(i) for i in range(first_min, first_max + 1)))

    print("\nOrdered from smallest to largest, the slopes are:")
    for i in second_elements:
        for j in second_elements[i]:
            if j == origin:
                continue
            numerator = j[1] - origin[1]
            denominator = j[0] - origin[0]
            if denominator < 0:
                numerator = -numerator
                denominator = -denominator
            # 约分处理
            # 判断特殊情况
            if denominator == 0:
                # 垂直线，分母为0，表示无穷大斜率
                slope.add((float('inf'), 1))
                continue

            if numerator == 0:
                # 水平线，分子为0，斜率0/1
                slope.add((0, 1))
                continue

            else:
                gcd_n = gcd(abs(numerator), abs(denominator))
                numerator = numerator // gcd_n
                denominator = denominator // gcd_n
                slope.add((numerator, denominator))

    inf_slopes = [f for f in slope if f[0] == float('inf')]
    normal_slopes = [f for f in slope if f[0] != float('inf')]

    # 排序
    sorted_fractions = sorted(normal_slopes, key=lambda x: x[0] / x[1])

    # 生成输出
    fraction_strs = [f"{i}/{j}" for i, j in sorted_fractions]
    inf_strs = [f"inf/1" for _ in inf_slopes]

    # 合并输出
    all_slopes = fraction_strs + inf_strs

    print(", ".join(all_slopes))

    # REPLACE PASS ABOVE WITH YOUR CODE


slopes(1233331, 3333334)
