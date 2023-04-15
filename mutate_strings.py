first_word = input()
second_word = input()

first_list = [s for s in first_word]
second_list = [s for s in second_word]

for i in range(len(first_list)):
    if first_list[i] != second_list[i]:
        first_list[i] = second_list[i]
        print("".join(first_list))
