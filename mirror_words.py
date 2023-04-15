import re

text = input()

pattern = r"(@|#)([A-Za-z]{3,})(\1\1)([A-Za-z]{3,})\1"

matches = re.finditer(pattern, text)
list_of_matches = {}
counter = 0

for match in matches:
    counter += 1
    first_word = match.group(2)
    second_word = match.group(4)
    if first_word == second_word[::-1]:
        list_of_matches[first_word] = second_word

if counter == 0:
    print("No word pairs found!")

elif counter > 0:
    print(f"{counter} word pairs found!")

if len(list_of_matches) == 0:
    print("No mirror words!")


elif len(list_of_matches) > 0:
    output = ""
    print("The mirror words are:")
    for word_1, word_2 in list_of_matches.items():
        output += f"{word_1} <=> {word_2}, "
    output = output[0:-2]
    print(output)
