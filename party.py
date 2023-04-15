class Party:
    def __init__(self):
        self.people = []
        self.counter = 0

    def get_info(self):
        return f"""Going: {", ".join(self.people)}
Total: {self.counter}"""


party = Party()
command = input()
while command != "End":
    party.people.append(command)
    party.counter += 1

    command = input()


print(party.get_info())
