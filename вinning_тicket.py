tickets = [s.strip() for s in input().split(', ')]
winning_symbols = ['@', '#', '$', '^']
for ticket in tickets:
    if len(ticket) < 20:
        print("invalid ticket")
        continue
    left_side = ticket[:10]
    right_side = ticket[10:]
    left_winning_variable = []
    right_winning_variable = []
    symbol = ""

    for index in range(0, len(left_side)):

        if left_side[index] in winning_symbols:
            left_winning_variable.append(left_side[index])
            symbol = left_side[index]

    for index in range(0, len(right_side)):

        if right_side[index] in winning_symbols:
            right_winning_variable.append(left_side[index])

    if len(left_winning_variable) == len(right_winning_variable):
        if len(left_winning_variable) == 10 and len(right_winning_variable) >= 10:
            print(f'ticket "{"".join(left_side + right_side)}" - 10{symbol} Jackpot!')
        elif 6 <= len(left_winning_variable) < 10 and 6 <= len(right_winning_variable) < 10:
            print(f'ticket "{"".join(left_side + right_side)}" - 6{symbol}')
        else:
            print(f'ticket "{"".join(left_side + right_side)}" - no match')
    else:
        print(f'ticket "{"".join(left_side + right_side)}" - no match')



