command = input().split(":")
products_in_stock = {}
while command[0] != "statistics":
    key = command[0]
    value = command[1]
    if key in products_in_stock:
        products_in_stock[key] += int(value)
        command = input().split(":")
        continue
    products_in_stock[key] = int(value)
    command = input().split(":")
print("Products in stock:")
total_quantity = 0
for k, v in products_in_stock.items():
    print(f"- {k}: {v}")
    total_quantity += int(v)
total_products = len(products_in_stock)
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")