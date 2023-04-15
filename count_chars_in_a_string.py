text = input().split()
letter_list = []
dictionary = {}
for word in text:
    for letter in word:
        letter_list.append(letter)

for letter in letter_list:
    if letter not in dictionary:
        dictionary[letter] = 0
    dictionary[letter] += 1

[print(f"{k} -> {v}") for k, v in dictionary.items()]