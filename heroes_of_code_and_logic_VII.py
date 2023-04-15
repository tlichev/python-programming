num = int(input())
hero_dict = {}

for _ in range(num):
    hero_data = input().split()
    hero_name = hero_data[0]
    hp = (hero_data[1])
    mp = (hero_data[-1])
    hero_dict[hero_name] = []
    hero_dict[hero_name]. append(int(hp))
    hero_dict[hero_name]. append(int(mp))

    # if hp > 100:
    #     hp = 100
    # if mp > 200:
    #     mp = 200
command = input().split(" - ")
while command[0] != "End":
    if command[0] == "CastSpell":
        hero = command[1]
        mp_needed = int(command[2])
        spell_name = command[-1]
        if hero in hero_dict:
            if hero_dict[hero][1] >= mp_needed:
                hero_dict[hero][1] -= mp_needed
                print(f"{hero} has successfully cast {spell_name} and now has {hero_dict[hero][1]} MP!")
            else:
                print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif command[0] == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[-1]
        if hero in hero_dict:
            hero_dict[hero][0] -= damage
            if hero_dict[hero][0] > 0:
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {hero_dict[hero][0]} HP left!")
            elif hero_dict[hero][0] <= 0:
                print(f"{hero} has been killed by {attacker}!")
                del hero_dict[hero]
    elif command[0] == "Recharge":
        hero = command[1]
        amount = int(command[2])
        if hero in hero_dict:
            mpp = hero_dict[hero][1]
            hero_dict[hero][1] += amount
            if hero_dict[hero][1] > 200:
                hero_dict[hero][1] = 200
                amount = 200 - mpp
                print(f"{hero} recharged for {amount} MP!")
            else:
                print(f"{hero} recharged for {amount} MP!")
    elif command[0] == "Heal":
        hero = command[1]
        amount = int(command[2])
        if hero in hero_dict:
            hpp = hero_dict[hero][0]
            hero_dict[hero][0] += amount
            if hero_dict[hero][0] > 100:
                hero_dict[hero][0] = 100
                amount = 100 - hpp
                print(f"{hero} healed for {amount} HP!")
            else:
                print(f"{hero} healed for {amount} HP!")
    command = input().split(" - ")

hero_dict = sorted(hero_dict.items(), key=lambda x: (-x[1][0], x[0]))


for k, v in hero_dict:
    print(k)
    print(f"  HP: {v[0]}")
    print(f"  MP: {v[1]}")
