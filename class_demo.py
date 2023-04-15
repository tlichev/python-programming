class Person:
    def __init__(self, first_name, last_name, age=0):
        self.firs_name = first_name
        self.lastname = last_name
        self.age = age
        self.something = []

    def get_info(self):
        return f"""{self.firs_name}
{self.lastname}
{self.age}"""


person_one = Person("gosho", "georgiev", 22)
print(person_one.get_info())

new_name = input()
person_one.firs_name = new_name
print(person_one.get_info())

for i in range(1, 6):
    something = input()
    person_one.something.append(something)

print(person_one.something)




