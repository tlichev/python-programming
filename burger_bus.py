number_cities = int(input())

total_needed_money = 0
total_owner_expenses = 0
for i in range(1, number_cities + 1):
    name_of_city = input()
    needed_money = float(input())
    owner_expenses = float(input())
    if i % 3 == 0:
        owner_expenses += 0.5 * owner_expenses

    elif i % 5 == 0:
        needed_money -= 0.10 * needed_money

    earned_money = needed_money - owner_expenses
    print(f'In {name_of_city} Burger Bus earned {earned_money:.2f} leva.')
    total_owner_expenses += owner_expenses
    total_needed_money += needed_money

total_earned_money = total_needed_money - total_owner_expenses
print(f'Burger Bus total profit: {total_earned_money:.2f} leva.')
