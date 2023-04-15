friend = input().split(", ")

command = input().split()
while command[0] != "Report":
    action = command[0]
    name = command[1:]

    if action == "Blacklist":
        current_name = name[0]
        if friend.count(current_name) >= 1:
            index_name = friend.index(current_name)
            friend.pop(index_name)
            friend.insert(index_name, "Blacklisted")
            print(f"{current_name} was blacklisted.")
        else:
            print(f"{current_name} was not found.")

    elif action == "Error":
        current_index = int(name[0])
        current_name = friend[current_index]
        if 0 <= current_index < len(friend):
            if friend[current_index] != "Blacklisted":
                if friend[current_index] != "Lost":
                    print(f"{current_name} was lost due to an error.")
                friend.pop(current_index)
                friend.insert(current_index, "Lost")

    elif action == "Change":
        current_index = int(name[0])
        new_name = name[1]
        if 0 <= current_index < len(friend):
            current_name = friend[current_index]
            friend.pop(current_index)
            friend.insert(current_index, new_name)
            print(f"{current_name} changed his username to {new_name}.")

    command = input().split()

blacklisted_names = 0
lost_names = 0

for i in friend:
    if i == "Blacklisted":
        blacklisted_names += 1
    elif i == "Lost":
        lost_names += 1

print(f'Blacklisted names: {blacklisted_names}')
print(f'Lost names: {lost_names}')
print(" ".join(friend))

