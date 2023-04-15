dictionary = {}
counter = 0
while True:
    name_num = input().split("-")
    if len(name_num) == 1:
        counter = name_num
        break
    for i in range(0, len(name_num), 2):
        if name_num[i] not in name_num:
            dictionary[i] = 0
        dictionary[name_num[i]] = (name_num[i + 1])

counter = int("".join(counter))
for c in range(0, counter):
    name = input()
    if name not in dictionary:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {dictionary[name]}")
