command = input().split()
dict_hero = {}

while command[0] != "End":
    if command[0] == "Enroll":
        hero_name = command[-1]
        if hero_name in dict_hero:
            print(f"{hero_name} is already enrolled.")
        elif hero_name not in dict_hero:
            dict_hero[hero_name] = []
    elif command[0] == "Learn":
        hero_name = command[1]
        spell_name = command[-1]
        if hero_name not in dict_hero:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in dict_hero:
            if spell_name in dict_hero[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                dict_hero[hero_name].append(spell_name)
    elif command[0] == "Unlearn":
        hero_name = command[1]
        spell_name = command[-1]
        if hero_name not in dict_hero:
            print(f"{hero_name} doesn't exist.")
        elif hero_name in dict_hero:
            if spell_name not in dict_hero[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")
            else:
                dict_hero[hero_name].remove(spell_name)

    command = input().split()
print("Heroes:")
dict_hero = sorted(dict_hero.items(), key=lambda x: (-len(x[1]), x[0]))
for hero, spell in dict_hero:
    if spell == []:
        print(f"== {hero}:")
    else:
        print(f"== {hero}: {', '.join(spell)}")