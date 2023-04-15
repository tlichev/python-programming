import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
text = input()
match = re.findall(pattern,text)
print(" ".join(match))