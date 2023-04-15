year = int(input()) + 1

while len(set(str(year))) != len(str(year)):
    i = len(set(str(year)))
    d = len(str(year))
    year += 1

print(year)