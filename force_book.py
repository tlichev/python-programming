command = input()
sides = {}
while command != "Lumpawaroo":
    if "|" in command:
        command.split(" | ")
        side = command.split(" | ")[0]
        name = command.split(" | ")[-1]
        if side not in sides:
            sides[side] = []
        sides[side].append(name)
    elif "->" in command:
        command.split(" -> ")
        side = command.split(" -> ")[-1]
        name = command.split(" -> ")[0]
        for k, v in sides.items():
            if name in v:
                sides[k].remove(name)
            sides[side].append(name)
            print(f"{name} joins the {side} side!")



    command = input()
print(sides)