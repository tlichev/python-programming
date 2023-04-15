import re

string = input().lower()
search = input().lower()
pattern = fr"\b{search}\b"
matches = re.findall(pattern, string)
print(len(matches))