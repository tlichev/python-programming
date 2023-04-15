concealed_message = input()
command = input()
while command != "Reveal":
    action = command.split(":|:")
    if action[0] == "InsertSpace":
        list_char =[s for s in concealed_message]
        index = int(action[-1])
        list_char.insert(index, " ")
        concealed_message = "".join(list_char)

        print(concealed_message)
    elif action[0] == "Reverse":
        substring = action[-1]
        if substring not in concealed_message:
            print("error")
        elif substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "",1)
            reversed_substring = substring[::-1]
            concealed_message += reversed_substring
            print(concealed_message)
    elif action[0] == "ChangeAll":
        new_str = ""
        substring = action[1]
        replacement = action[-1]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)


    command = input()
print(f"You have a new text message: {concealed_message}")
