number = int(input())
dictionary =  {}

for count in range(0, number):
    command = input().split()
    if command[0] == "register":
        name = command[1]
        car_num = command[-1]
        if name not in dictionary:
            dictionary[name] = car_num
            print(f"{name} registered {car_num} successfully")
        elif name in dictionary:
            print(f"ERROR: already registered with plate number {car_num}")
    elif command[0] == "unregister":
        name = command[1]
        if name not in dictionary:
            print(f"ERROR: user {name} not found")
        elif name in dictionary:
            del dictionary[name]
            print(f"{name} unregistered successfully")

for k, v in dictionary.items():
    print(f"{k} => {v}")





