# Written by *** for COMP9021
#
# Encode 0 as 100.
# Given a strictly positive integer n that in base 2,
# reads as b_{1} ... b_{k},
# - encode -n as the integer that in base 2,
#   reads as b_{1}b_{1} ... b_{k}b_{k},
# - encode n as the integer that in base 2,
#   reads as 1b_{1}b_{1} ... b_{k}b_{k}.
# Encode the empty sequence as 0.
# Given an integer n, let the encoding of n also be the encoding of [n].
# Given a list L = [n_{1}, ..., n_{i}] of integers with i > 1,
# encode L as the integer that in base 2, reads as
# c_{1}s_{1}...c_{i-i}s_{i-1}c_{i} where
# - c_1 is the sequence of bits that encodes n_{1}, ...,
#   c_{i} is the sequence of bits that encodes n_{i},
# - s_{1} is 10 if n_2 < 0, and s_{1} is 0 otherwise, ...,
#   s_{i-1} is 10 if n_{i} < 0, and s_{i-1} is 0 otherwise.
#
# Implements a function encode() that takes a list of integers
# as argument, and returns its encoding.
#
# Implements a function decode() that takes an integer n as argument
# and returns None if n does not encode a list,
# and returns the list it encodes otherwise.
#
# Implements a function proportion_of_valid_codes() that takes
# either one integer n at least equal to 0 as argument
# or two integers m and n at least equal to 0 as arguments
# with n at least equal to m,
# that returns what the function says for potential codes
# ranging between 0 and n included in the first case,
# between m and n included in the second case.


import sys


def encode_a_num(num):
    if num == 0:
        return "100"

    binary_num = bin(abs(num))[2:]
    result = ''.join(d * 2 for d in binary_num)

    return "1" + result if num > 0 else result


def encode(L):
    if "[" not in str(L):
        return encode([L])
    if len(L) == 0:
        return 0

    encoded = []
    for number in L:
        encoded.append(encode_a_num(number))

    connect = []
    for number in L[1:]:
        if number < 0:
            connect.append("10")
        else:
            connect.append("0")

    show_result = ""
    for item in range(len(connect)):
        show_result += encoded[item] + connect[item]
    show_result += encoded[-1]

    return int(show_result, 2)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


def decode_a_num(num):
    if len(num) < 2 or num[0] == "0":
        return None
    if num[:3] == "100" and num != "100":
        return None
    sign = -1
    if num[0] == "1" and len(num) % 2 == 1:
        sign = 1
        num = num[1:]
    bin_num = ""
    for item in range(0, len(num), 2):
        bin_num += num[item]
    return sign * int(bin_num, 2)


def get_signed_bin(bin_num, is_positive):
    one_num = ""
    start = 1 if is_positive else 0
    while start + 1 < len(bin_num) and bin_num[start] == bin_num[start + 1]:
        one_num += bin_num[start] * 2
        start += 2
    return ("1" if is_positive else "") + one_num


def decode_first(bin_num, next_positive):
    lst = []
    while bin_num:
        number = get_signed_bin(bin_num, next_positive)
        real_num = decode_a_num(number)
        if real_num is None:
            return None
        else:
            lst.append(real_num)
        length = len(number)
        bin_num = bin_num[length:]
        if len(bin_num) == 0:
            break
        if bin_num[0] == "0":
            next_positive = True
            bin_num = bin_num[1:]
        elif bin_num[:2] == "10":
            next_positive = False
            bin_num = bin_num[2:]
        else:
            return None
        if bin_num == "":
            return None
    return lst


def decode(n):
    if n == 0:
        return []
    if n < 0:
        return None
    binary_num = bin(n)[2:]
    result = decode_first(binary_num, True)
    if result is not None:
        return result
    result = decode_first(binary_num, False)
    if result is not None:
        return result
    return None
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


def proportion_of_valid_codes(*args):
    if len(args) == 1:
        start = 0
        end = args[0] + 1
    else:
        start = args[0]
        end = args[1] + 1
    count = 0
    for number in range(start, end):
        if decode(number) is not None:
            count += 1
    return count / (end - start)
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS
