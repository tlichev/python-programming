students = input().split(":")
courses = {}
student = []
command = None


while True:
    if len(students) == 1:
        command = students[0]
        break
    course = students[-1]
    name = students[0]
    id = students[1]

    if course not in courses:
        courses[course] = {}
    courses[course][id] = name
    students = input().split(":")
command = command.replace("_", " ")
res = courses[command]
for k, v in res.items():
    print(f"{v} - {k}" )