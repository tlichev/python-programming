def upper_or_lower(expression):
    num = int(expression[1:-1])
    if expression[0].isupper():
        index = upper_alphabet_list.index(expression[0]) + 1
        res = num / index
        if expression[-1].isupper():
            index = upper_alphabet_list.index(expression[-1]) + 1
            res -= index
        else:
            index = lower_alphabet_list.index(expression[-1]) + 1
            res += index
    else:
        index = lower_alphabet_list.index(expression[0]) + 1
        res = num * index
        if expression[-1].isupper():
            index = upper_alphabet_list.index(expression[-1]) + 1
            res -= index
        else:
            index = lower_alphabet_list.index(expression[-1]) + 1
            res += index
    return res


string_list = input().split()
total_sum = 0
upper_alphabet_list = ["A", "B", "C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_alphabet_list = ["a", "b", "c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for string in string_list:
    total_sum += upper_or_lower(string)
print(f'{total_sum:.2f}')
