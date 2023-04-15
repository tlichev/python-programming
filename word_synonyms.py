num = int(input())
# word = input()
dictionary = {}

for number in range(0, num):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(synonym)
for word, list in dictionary.items():
    print(f'{word} - {", ".join(list)}')

