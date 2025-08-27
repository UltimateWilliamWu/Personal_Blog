# words.py

sentence = "In the loveliest town of all, where the houses were white and high and the elms trees were green and higher than the houses, where the front yards were wide and pleasant and the back yards were bushy and worth finding out about, where the streets sloped down to the stream and the stream flowed quietly under the bridge, where the lawns ended in orchards and the orchards ended in fields and the fields ended in pastures and the pastures climbed the hill and disappeared over the top toward the wonderful wide sky, in this loveliest of all towns Stuart stopped to get a drink of sarsaparilla."

import string

# Remove punctuation (commas and full stops)
cleaned_sentence = sentence.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = cleaned_sentence.split()

# Calculate total length of all words
total_length = sum(len(word) for word in words)

# Calculate average word length
average_length = total_length / len(words)

# Print result to two decimal places
print(f"{average_length:.2f}")

sales = "2543,4,4.34;5463,7,8.31;7765,10,1.23;9833,9,34.12;5056,4,5.67;7657,10,4.23;3343,7,2.98;3778,9,9.27;1118,5,8.23;3873,3,4.45;6588,2,5.67;5778,6,3.41;7765,11,2.23;9343,8,4.12;5057,5,4.67;7657,5,4.23;3356,7,4.98;3776,8,8.27;1228,5,7.23;3873,2,4.50"

sales = sales.strip(';')
groups = sales.split(';')
result = [group.split(",") for group in groups]
total = 0
for r in result:
    total += float(r[1]) * float(r[2])
print(total)