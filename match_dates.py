import re

text = input()
pattern = r"(\d{2})(.|\/|-)([A-Z][a-z]{2})(\2)(\d{4})"
matches = re.finditer(pattern, text)

for mach in matches:
    print(f'Day: {mach[1]}, Month: {mach[3]}, Year: {mach[5]}')