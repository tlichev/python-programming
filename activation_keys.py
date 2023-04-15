activation_key = input()
command = input().split(">>>")

while command[0] != "Generate":
    if command[0] == "Contains":
        substring = command[-1]
        if substring not in activation_key:
            print("Substring not found!")
        else:
            print(f"{activation_key} contains {substring}")

    elif command[0] == "Flip":
        upper_or_lower, start_index, end_index = command[1::]
        start_index = int(start_index)
        end_index = int(end_index)
        if upper_or_lower == "Upper":
            upper_word = activation_key[start_index:end_index].upper()
            activation_key = activation_key[0:start_index] + upper_word + activation_key[end_index::]
            print(activation_key)
        else:
            lower_word = activation_key[start_index:end_index].lower()
            activation_key = activation_key[0:start_index] + lower_word + activation_key[end_index::]
            print(activation_key)
    elif command[0] == "Slice":
        start_index, end_index = command[1::]
        start_index = int(start_index)
        end_index = int(end_index)
        word_to_remove = activation_key[start_index:end_index]
        activation_key = activation_key.replace(word_to_remove, "")
        print(activation_key)


    command = input().split(">>>")

print(f"Your activation key is: {activation_key}")
#
# num = 90
# sum = 0
# while num > 0:
#     if num % 4 == 0:
#         sum += num
#     num -= 1
#
# print(sum)
