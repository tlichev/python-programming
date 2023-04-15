products = input().split()
store = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i+1]
    store[key] = int(value)
items = input().split()
for item in items:
    if item in store:
        print(f"We have {store[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")