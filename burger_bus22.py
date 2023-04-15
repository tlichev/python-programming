number_of_cities = int(input())

total_earn = 0
total_expenses = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    earn = float(input())
    expenses = float(input())

    if city % 15 == 0:
        earn -= earn * 0.1

    elif city % 3 == 0:
        expenses += 0.5 * expenses

    elif city % 5 == 0:
        earn -= earn * 0.1



    money = earn - expenses
    print(f'In {city_name} Burger Bus earned {money:.2f} leva.')
    total_earn += earn
    total_expenses += expenses

total_money = total_earn - total_expenses
print(f'Burger Bus total profit: {total_money:.2f} leva.')