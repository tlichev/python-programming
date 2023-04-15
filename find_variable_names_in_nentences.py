import re

patten = r"\b_([a-z]+|[A-Z]+[0-9]+)\b"
string = input()

matches = re.findall(patten, string)
print(",".join(matches))