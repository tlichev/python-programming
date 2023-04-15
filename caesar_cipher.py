message = input()
encrypted_version = ""

for ch in message:
    num = ord(ch) + 3
    encrypted_version += chr(num)
print(encrypted_version)