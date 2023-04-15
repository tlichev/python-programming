num = int(input())
dictionary = {}
students = []

for i in range(0, num):
    name = input()
    grade = input()
    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(float(grade))


for k, v in dictionary.items():
    if len(dictionary[k]) > 1:
        average = 0
        for i in v:
            average += i
        dictionary[k] = [average / len(v)]

new_dictionary = {}
for k, v in dictionary.items():
    for i in v:
        if i >= 4.50:
            new_dictionary[k] = i


sorted_students = sorted(new_dictionary.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_students:
    print(f"{key} -> {value:.2f}")