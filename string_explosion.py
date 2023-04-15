string = input()
new_string = ""
explosion_power = 0

for index in range(len(string)):
    if string[index] != ">" and explosion_power > 0:
        explosion_power -= 1
    elif string[index] == ">":
        explosion_power += int(string[index+1])
        new_string += string[index]
    else:
        new_string += string[index]

print(new_string)





