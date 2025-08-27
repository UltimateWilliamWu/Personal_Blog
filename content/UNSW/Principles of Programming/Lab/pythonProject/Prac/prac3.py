# %load modulo_4.py
# Written by Eric Martin for COMP9021


from random import seed, randrange
import sys

# Prompts the user for an integer to provide as argument to the
# seed() function.
try:
    arg_for_seed = int(input('Feed the seed with an integer: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
# Prompts the user a strictly positive number, nb_of_elements.
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
# Generates a list of nb_of_elements random integers between 0 and 99.
L = [randrange(20) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
print()
result = {0: [], 5: [], 10: [], 15: []}
for numbers in L:
    if 0 <= numbers <= 4:
        result[0].append(numbers)
    elif 5 <= numbers <= 9:
        result[5].append(numbers)
    elif 10 <= numbers <= 14:
        result[10].append(numbers)
    elif 15 <= numbers <= 19:
        result[15].append(numbers)
for key, value in result.items():
    if value:
        print(f'There is {len(value)} element between {key} and {key + 4}.')
    else:
        print(f'There is no element between {key} and {key + 4}.')
