command = input().split()

chat = []
while command[0] != "end":
    action = command[0]
    message = command[1:]

    if action == "Chat":
        current = message[0]
        chat.append(message[0])
    elif action == "Delete":
        current = message[0]
        if chat.count(current) >= 1:
            chat.remove(current)
    elif action == "Edit":
        old_message = message[0]
        new_message = message[1]
        if chat.count(old_message) >= 1:
            index_old_message = chat.index(old_message)
            chat.pop(index_old_message)
            chat.insert(index_old_message, new_message)
    elif action == "Pin":
        current = message[0]
        if chat.count(current) >= 1:
            index_message = chat.index(current)
            delete_message = chat.pop(index_message)
            chat.append(delete_message)
    elif action == "Spam":
        spam_list = message
        chat.extend(spam_list)
    command = input().split()


print("\n".join(chat))



