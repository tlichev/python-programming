command = input()
while command != "end":
    reversed_command = command[::-1]
    print(f"{command} = {reversed_command}")
    command = input()
