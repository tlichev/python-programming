command = input().split(" : ")
dictionary = {}
while command[0] != "end":
    course = command[0]
    name = command[1]
    if course not in dictionary:
        dictionary[course] = []
    dictionary[course].append(name)
    command = input().split(" : ")

sorted_dictionary = sorted(dictionary.items(), key=lambda kvpt: len(kvpt[1]), reverse=True )

for k, v in sorted_dictionary:
    print(f'{k}: {len(v)}')
    for i in sorted(v):
        print(f"-- {i}")

