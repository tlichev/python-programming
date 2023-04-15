product_info = input().split()
products = {}

while product_info[0] != "buy":
    name = product_info[0]
    price = product_info[1]
    quantity = float(product_info[-1])
    if name not in products:

        products[name] = []
        products[name].insert(0, price)
        products[name].insert(1, quantity)
    elif name in products:
        products[name].pop(0)
        products[name].insert(0, price)

        products[name][1] += quantity

    product_info = input().split()

for item, list_values in products.items():
    price = float(list_values[0]) * float(list_values[-1])
    print(f"{item} -> {price:.2f}")
