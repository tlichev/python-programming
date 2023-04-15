class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner == None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        elif self.owner != None:
            return "Car already sold"

    def sell(self):
        if self.owner != None:
            self.owner = None
        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"

vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
vehicle.buy(15000, "Peter")
vehicle.buy(35000, "George")
print(vehicle)
vehicle.sell()
print(vehicle)

p = input()
# Sorry, not enough money
# Successfully bought a car. Change: 5000.00
# BMW car is owned by: George
# BMW car is on sale: 30000
