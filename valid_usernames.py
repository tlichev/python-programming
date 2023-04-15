def is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def symbols_are_valid(username):
    for ch in username:
        if not(ch.isalnum() or ch == '-' or ch == '_'):
            return False
    return True


def no_redundant_symbols(username):
    for user in username:
        if user == " ":
            return False
    return True


def username_is_valid(username):
    if is_valid(username) and symbols_are_valid(username) and no_redundant_symbols(username):
        return True
    return False


usernames = input().split(", ")

for name in usernames:
    if username_is_valid(name):
        print(name)

