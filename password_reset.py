text = input()
command = input()

password = text

while command != "Done":
    action = command.split()
    if action[0] == "TakeOdd":
        curr_pass = password
        password = ""
        for index in range(0, len(curr_pass)):
            if index % 2 == 1:
                letter = curr_pass[index]
                password += letter
        print(password)
    elif action[0] == "Cut":
        index = int(action[1])
        length = int(action[-1])
        text_to_replace = password[index:index + length]
        password = password.replace(text_to_replace, "", 1)
        print(password)

    elif action[0] == "Substitute":
        substring = action[1]
        substitute = action[-1]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()


print(f"Your password is: {password}")

