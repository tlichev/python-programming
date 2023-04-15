quantity = int(input())
days = int(input())

christmas_spirit = 0
total_price = 0
current_day = 0
while current_day != days:
    current_day += 1
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        christmas_spirit += 5
        total_price += 2 * quantity
    if current_day % 3 == 0:
        christmas_spirit += 13
        total_price += (5 + 3) * quantity
    if current_day % 5 == 0:
        christmas_spirit += 17
        total_price += 15 * quantity
    if current_day % 15 == 0:
        christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        total_price += 3 + 5 + 15

        if current_day == days:
            christmas_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")
