import re

pattern = r"(\+359)( |-)2(\2)\d{3}(\2)\d{4}\b"
test = input()
match = re.finditer(r"\+359( |-)2+(\1)\d{3}(\1)\d{4}\b", test)
numbers = []
for m in match:
    num = "".join(m.group(0))
    numbers.append(num)

print(", ".join(numbers))




