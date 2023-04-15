num = int(input())
car_data = {}

for _ in range(num):
    data = input().split("|")
    car = data[0]
    mileage = data[1]
    fuel = data[2]
    car_data[car] = []
    car_data[car].append(int(mileage))
    car_data[car].append(int(fuel))

command = input().split(" : ")
while command[0] != "Stop":
    if command[0] == "Drive":
        model = command[1]
        distance = int(command[2])
        fuel = int(command[-1])
        if car_data[model][1] >= fuel:
            car_data[model][1] -= fuel
            car_data[model][0] += distance
            print(f"{model} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        elif car_data[model][1] < fuel:
            print("Not enough fuel to make that ride")
        if car_data[model][0] >= 100000:
            del car_data[model]
            print(f"Time to sell the {model}!")

    elif command[0] == "Refuel":
        model = command[1]
        fuel = int(command[-1])
        more_fuel = car_data[model][1]
        car_data[model][1] += fuel
        if car_data[model][1] > 75:
            car_data[model][1] = 75
            fuel = 75 - more_fuel
            print(f"{model} refueled with {fuel} liters")
        else:

            print(f"{model} refueled with {fuel} liters")

    elif command[0] == "Revert":
        model = command[1]
        kilometers = int(command[-1])
        car_data[model][0] -= kilometers
        if car_data[model][0] < 10000:
            car_data[model][0] = 10000
        else:
            print(f"{model} mileage decreased by {kilometers} kilometers")
    command = input().split(" : ")

car_data = sorted(car_data.items(), key=lambda x: (-x[1][0], x[0]))

for car, data in car_data:
    print(f"{car} -> Mileage: {data[0]} kms, Fuel in the tank: {data[1]} lt.")


