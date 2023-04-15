class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, kind_of_animal, animal):

        if kind_of_animal == "mammal":
            self.mammals.append(animal)
        elif kind_of_animal == "fishes":
            self.fishes.append(animal)
        elif kind_of_animal == "birds":
            self.birds.append(animal)
        Zoo.__animals += 1

    def get_info(self, species):
        result =""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fishes":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "birds":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
number = int(input())
zoo = Zoo(name_of_zoo)
for num in range(1, number + 1):
    line = input().split()
    kind_of_animal = line[0]
    animal = line[1]

    zoo.add_animal(kind_of_animal, animal)

species = input()
print(zoo.get_info(species))
