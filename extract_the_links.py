import re

pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
text = input()
valid = []

while text != "":
    matches = re.finditer(pattern, text)

    for match in matches:
        valid.append(match.group(1))
    text = input()
for i in valid:
    print(i)