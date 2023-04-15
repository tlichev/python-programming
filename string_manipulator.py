text = input()

command = input().split()
while command[0] != "End":
    if command[0] == "Translate":
        char = command[1]
        replacement = command[-1]
        text = text.replace(char, replacement)
        print(text)
        pass
    elif command[0] == "Includes":
        substring = command[-1]
        flag = False
        if substring in text:
            flag = True
        print(flag)
    elif command[0] == "Start":
        substring = command[-1]
        length = len(substring)
        flag = False
        new_string = text[0:length]
        if text[0:length] == substring:
            flag = True
        print(flag)

    elif command[0] == "Lowercase":
        text = text.lower()
        print(text)
    elif command[0] == "FindIndex":
        char = command[1]
        new_text = text[::-1]
        new_text = new_text.replace(char, "$", 1)
        new_text = new_text[::-1]
        index = new_text.find("$")
        print(index)

    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[-1])
        text = text[0:start_index] + "" + text[start_index+count::]
        print(text)

    command = input().split()