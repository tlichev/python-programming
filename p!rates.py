city_data = input().split("||")
dict_cities = {}
while city_data[0] != "Sail":

    city = city_data[0]
    population = city_data[1]
    gold = city_data[-1]

    if city in dict_cities:
        dict_cities[city][0] += int(population)
        dict_cities[city][1] += int(gold)
    else:
        dict_cities[city] = []
        dict_cities[city].append(int(population))
        dict_cities[city].append(int(gold))
    # if city in dict_cities:
        # dict_cities[city][0] += int(population)
        # dict_cities[city][1] += int(gold)

    city_data = input().split("||")
# print(dict_cities)

command = input().split("=>")
while command[0] != "End":
    if command[0] == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[-1])
        dict_cities[town][0] -= people
        dict_cities[town][1] -= gold
        if dict_cities[town][0] == 0 or dict_cities[town][1] == 0:
            del dict_cities[town]
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    elif command[0] == "Prosper":
        town = command[1]
        gold = int(command[-1])
        if gold >= 0:
            dict_cities[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dict_cities[town][1]} gold.")

        else:
            print("Gold added cannot be a negative number!")
        pass

    command = input().split("=>")

print(f"Ahoy, Captain! There are {len(dict_cities)} wealthy settlements to go to:")
dict_cities = sorted(dict_cities.items(), key=lambda kvpt: (-kvpt[1][1], kvpt[0]))
for city, data in dict_cities:
    print(f"{city} -> Population: {data[0]} citizens, Gold: {data[1]} kg")
