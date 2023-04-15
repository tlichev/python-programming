command = input()
list = []
dictionary = {}
while command != 'stop':

    list.append(command)
    command = input()


for i in range(0, len(list), 2):
    if list[i] not in dictionary:
        dictionary[list[i]] = 0
    dictionary[list[i]] += int(list[i+1])


for k, v in dictionary.items():
    print(f"{k} -> {v}")