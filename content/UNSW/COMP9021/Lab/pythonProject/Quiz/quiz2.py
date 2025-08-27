# Written by *** for COMP9021
#
# Defines a function f() that takes a list as argument,
# that you can assume is a permutation of {0, ..., n}
# for some integer n >= 0.
# The function returns a list that is defined according
# to the example where the input list is
# [0, 2, 12, 3, 4, 6, 1, 9, 7, 10, 8, 11, 5].
# - Values smaller than indexes:
#   The index of 1 is 6, the index of 7 is 8,
#   the index of 8 is 10, and the index of 5 is 12.
# - Values equal to indexes: 0, 3, 4, 11.
# - Values larger than indexes:
#   The index of 2 is 1, the index of 12 is 2,
#   the index of 6 is 5, the index of 9 is 7
#   and the index of 10 is 9.
# [1, 7, 8, 5, 0, 3, 4, 11, 2, 12, 6, 9, 10] is returned.
#
# Defines a function g() that takes a list as argument,
# that you can assume is a permutation of {1, ..., n}
# for some integer n >= 1.
# The function returns a dictionary D, defined according
# to the example where the input list is
# [8, 9, 2, 6, 4, 5, 3, 1, 10, 7].
# - The first integer that comes after 8 in the list and that is
#   greater than 8 is 9, and the first integer that comes after 9
#   in the list and that is greater than 9 is 10.
#   D maps 1 to [0, 8, 9, 10].
# - What is left of the list is [2, 6, 4, 5, 3, 1, 7]
#   The first integer that comes after 2 in the list and that is
#   greater than 2 is 6, and the first integer that comes after 6
#   in the list and that is greater than 6 is 7.
#   D maps 2 to [0, 2, 6, 7].
# - What is left of the list is [4, 5, 3, 1]
#   The first integer that comes after 4 in the list and that is
#   greater than 4 is 5.
#   D maps 3 to [0, 4, 5].
# - What is left of the list is [3, 1]
#   No integer in the list after 3 is greater than 3.
#   D maps 4 to [0, 3].
# - What is left of the list is [1]
#   D maps 5 to [0, 1].

def f(L):
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    smaller_value = []
    equal_value = []
    bigger_value = []
    for index in range(len(L)):
        if index > L[index]:
            smaller_value.append(L[index])
        if index == L[index]:
            equal_value.append(L[index])
        if index < L[index]:
            bigger_value.append(L[index])
    return smaller_value + equal_value + bigger_value


def g(L):
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    count_map = 1
    result_map = {}
    while L:
        result = [0]
        current_number = 0
        remaining_numbers = []
        for number in range(len(L)):
            if L[number] > current_number:
                result.append(L[number])
                current_number = L[number]
            else:
                remaining_numbers.append(L[number])
        result_map[count_map] = result
        count_map += 1
        L = remaining_numbers
    return dict(result_map)


print(f([]))
