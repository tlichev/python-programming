import re

text = input()
pattern = r"(#|\|)([A-Z]*[a-z]* *[A-Z][a-z]*)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1([0-9]{1,})\1"

matches = re.finditer(pattern, text)
calories_counter = 0
list_matches = []
for match in matches:
    calories = match.group(4)
    calories_counter += int(calories)
    list_matches.append(match.group())

days_left = int(calories_counter / 2000)
print(f"You have food to last you for: {days_left} days!")

for product in list_matches:
    pattern = r"(#|\|)([A-Z]*[a-z]* *[A-Z][a-z]*)\1([0-9][0-9]\/[0-9][0-9]\/[0-9][0-9])\1([0-9]{1,})\1"
    product_data = re.search(pattern, product)
    print(f"Item: {product_data.group(2)}, Best before: {product_data.group(3)}, Nutrition: {product_data.group(4)}")
