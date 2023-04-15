def join_function(string_list):
    return "".join(string_list)


string = input("Paste string here -->")

digit_list = []
char_list = []
special_symbols = []

for ch in string:
    if ch.isdigit():
        digit_list.append(ch)
    elif ch.isalpha():
        char_list.append(ch)
    else:
        special_symbols.append(ch)

print(join_function(digit_list))
print(join_function(char_list))
print(join_function(special_symbols))
