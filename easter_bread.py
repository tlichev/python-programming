budget = float(input())
price_flour_1kg = float(input())
price_eggs = price_flour_1kg * 0.75
liter1_milk = (price_flour_1kg * 0.25) + price_flour_1kg
ml250_milk = liter1_milk * 0.250

one_bread = price_flour_1kg + price_eggs + ml250_milk
bread_counter = 0
egg_counter = 0
while budget >= one_bread:
    budget -= price_flour_1kg + price_eggs + ml250_milk
    bread_counter += 1
    egg_counter += 3
    if bread_counter % 3 == 0:
        egg_counter -= bread_counter - 2


print(f"You made {bread_counter} loaves of Easter bread! Now you have {egg_counter} eggs and {budget:.2f}BGN left.")