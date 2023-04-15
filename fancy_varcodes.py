import re

num = int(input())

for _ in range(num):
    barcode = input()
    pattern = r"(@#{1,})[A-Z][A-Za-z0-9]{4,}[A-Z](@#{1,})"
    match = re.search(pattern, barcode)
    flag = False
    group = ""
    if match:
        barcode = match.group()
        for ch in barcode:
            if ch.isdigit():
                group += ch
                flag = True
        if flag:
            print(f"Product group: {group}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")



