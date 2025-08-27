# Written by *** for COMP9021
#
# Two functions to implement.
#
#
# The function frieze() takes an integers as argument,
# that you can assume is at least equal to 1;
# it prints out a "frieze", that note has no trailing
# spaces on any line.
#
#
# The function numbers() takes a string as argument,
# that you can assume is the name of a file that exists
# in the working directory.
#
# The file can contain anywhere any number of blank lines
# (that is, lines containing an arbitrary number of spaces
# and tabs--an empty line being the limiting case).
#
# Nonblank lines are always of the form:
# axb^c
# where a is a nonempty sequence of dots, b is an integer
# and c is a nonempty sequence of dots,
# with no space anywhere on the line,
# that represents
#      (number of dots in a) times (b to the power the number of dots in c)
# For instance, ..*-3^..... represents 2 x (-3 ^ 5), so -486.
# Note that ** is the Python operator for exponentiation.
#
# The function returns the (possibly empty) list of all such "numbers"
# (so there are as many elements in the list as nonempty lines in the file).
import re


def frieze(n):
    # start shape
    start = [
        "\\ ",
        " \\",
        " ||",
        "/  "
    ]

    # tower shape and repeat for n times according to the argument n
    tower = [
        " /\\ ",
        "/..\\",
        "  ||",
        "    "
    ]

    # end shape
    end = [
        " /",
        "/",
        "",
        "\\"
    ]

    # join shape with start tower end
    for i in range(len(start)):
        print(start[i] + tower[i] * n + end[i])
        # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE


def numbers(filename):
    results = []  # storing calculation

    with open(filename) as file:
        for line in file:
            line = line.strip()  # not including '\n'
            if not line:
                continue

            result = re.split(r'[x^]', line)  # using x or ^ as seperator
            a = result[0].count('.')  # `.` count as a
            b = int(result[1])  # b as an integer
            c = result[2].count('.')  # `.` count as  c
            calculation = a * b ** c  # calculate a * b^c
            results.append(calculation)  # storing the results

    return results
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


def numbers1(filename):
    results = []  # storing calculation

    with open(filename) as file:
        text = file.read().split("\n")
    for line in text:
        if " " not in line and "\t" not in line and "" != line:
            index_star = line.index("x")
            index_square = line.index("^")
            number_one = len(line[0:index_star])
            number_two = int(line[index_star + 1:index_square])
            number_three = len(line) - index_square - 1
            number = number_one * number_two ** number_three
            results.append(number)

    return results
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE


print(numbers("../test_1.txt"))
