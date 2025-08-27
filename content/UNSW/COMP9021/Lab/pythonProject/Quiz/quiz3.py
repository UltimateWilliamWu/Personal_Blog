import sys

try:
    n = int(input('Enter an integer: '))
    if not n:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

base3_result = ""
direction_sequence = []
arrow = ""
sign = '-' if n < 0 else '+'
n = abs(n)
while n != 0:
    digit = n % 3
    base3_result = str(digit) + base3_result
    # 选择箭头
    if digit == 0:
        arrow = "⇩" if sign == "-" else "⇧"  # ⇑ ⇓
    elif digit == 1:
        arrow = "⬂" if sign == "-" else "⬁"  # ⇖ ⇘
    elif digit == 2:
        arrow = "⬃" if sign == "-" else "⬀"  # ⇗ ⇙

    direction_sequence.append(arrow)
    n = n // 3

base3_result = sign + base3_result
direction_sequence_display = ' '.join(direction_sequence)
print(f"Your input in base 3 reads: {base3_result}\n")
print(f"This is how we will travel (reading digits from right to left):\n{direction_sequence_display}\n")
print("This is how we travelled:")
space_distance = 0
min_space = 0
for arrow in direction_sequence[1:]:
    if arrow == "⬂" or arrow == "⬀":
        space_distance += 1
    if arrow == "⬃" or arrow == "⬁":
        space_distance -= 1
    if space_distance < min_space:
        min_space = space_distance
space_numbers = abs(min_space)
result = [space_numbers * " " + direction_sequence[0]]
for arrow in direction_sequence[1:]:
    if arrow == "⬂" or arrow == "⬀":
        space_numbers += 1
    if arrow == "⬃" or arrow == "⬁":
        space_numbers -= 1
    result.append(space_numbers * " " + arrow)
if sign == "+":
    result.reverse()
for line in result:
    print(line)
