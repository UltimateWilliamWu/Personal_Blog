# Written by *** for COMP9021
#
# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n
#   is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together
#   with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing
# the standard form decomposition of the permutation into cycles
# (see wikepedia page on permutations for details).
# - A given cycle starts with the largest value in the cycle.
# - Cycles are given from smallest first value to largest first value.
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix
# and in-place uses, thanks to the __mul__() and __imul__() special methods,
# respectively.


class PermutationError(Exception):
    pass


class Permutation:
    def __init__(self, *args, length=None):
        if not args and length is None:
            self.numbers = []
            self.length = 0
        elif not args and isinstance(length, int) and length >= 0:
            self.numbers = list(range(1, length + 1))
            self.length = length
        elif args:
            if any(type(arg) is not int for arg in args):
                raise PermutationError("Cannot generate permutation from these arguments")
            if length is None:
                length = len(args)
            if len(args) != length or sorted(args) != list(range(1, length + 1)):
                raise PermutationError("Cannot generate permutation from these arguments")
            self.numbers = list(args)
            self.length = length
        else:
            raise PermutationError("Cannot generate permutation from these arguments")

        self._process_cycles()

    def __len__(self):
        return self.length
        # Replace pass above with your code

    def __repr__(self):
        nums_string = []
        for num in self.numbers:
            nums_string.append(str(num))
        return "Permutation(" + ", ".join(nums_string) + ")"
        # Replace pass above with your code

    def _process_cycles(self):
        visited = [False] * self.length
        self.cycles = []
        self.nb_of_cycles = 0

        for i in range(self.length):
            if not visited[i]:
                cycle = []
                j = i
                while not visited[j]:
                    visited[j] = True
                    cycle.append(j + 1)
                    j = self.numbers[j] - 1
                self.nb_of_cycles += 1
                max_val = max(cycle)
                max_idx = cycle.index(max_val)
                cycle = cycle[max_idx:] + cycle[:max_idx]
                self.cycles.append(cycle)
        self.cycles.sort()

    def __str__(self):
        result = ""
        for cycle in self.cycles:
            string_cycle = []
            for num in cycle:
                string_cycle.append(str(num))
            result += "(" + " ".join(string_cycle) + ")"
        return result if result != "" else "()"
        # Replace pass above with your code

    def __mul__(self, permutation):
        if len(self) != len(permutation):
            raise PermutationError("Cannot compose permutations of different lengths")
        numbers = [0] * self.length
        for index in range(self.length):
            numbers[permutation.numbers[index] - 1] = self.numbers[index]
        return Permutation(*numbers)
        # Replace pass above with your code

    def __imul__(self, permutation):
        if len(self) != len(permutation):
            raise PermutationError("Cannot compose permutations of different lengths")
        numbers = [0] * self.length
        for index in range(self.length):
            numbers[index] = permutation.numbers[self.numbers[index] - 1]
        self.numbers = numbers
        self._process_cycles()
        return self
        # Replace pass above with your code

    def inverse(self):
        result = [0] * self.length
        for index in range(self.length):
            number = index + 1
            new_index = self.numbers[index] - 1
            result[new_index] = number
        return Permutation(*result)
        # Replace pass above with your code

    # Insert helper functions, if needed




