import re

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
list = []
total_sum = 0
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        list.append(furniture)
        total_sum += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for i in list:
    print(i)
print(f"Total money spend: {total_sum:.2f}")