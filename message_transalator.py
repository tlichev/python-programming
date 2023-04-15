import re

num = int(input())
for _ in range(num):
    text = input()
    pattern = r"(!)([A-Z][a-z]{3,})\1:\[([A-Za-z]{8,})\]"

    match = re.search(pattern, text)

    if match:
        num_list = []
        message = match.group(3)
        for letter in message:
            num_list.append(str(ord(letter)))
        print(f"{match.group(2)}: {' '.join(num_list)}")

    else:
        print("The message is invalid")