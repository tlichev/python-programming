command = input().split(" -> ")
users = {}
while command[0] != "End":
    company_name = command[0]
    id = command[-1]
    if company_name not in users:
        users[company_name] = []
    users[company_name].append(id)

    command = input().split(" -> ")
company_users = {}
for k,v in users.items():
    company_users[k] = set(v)

sorted_users = dict(sorted(company_users.items(), key=lambda kvp: kvp[0]))

for company, ids in sorted_users.items():
    print(f'{company}')
    for id in sorted(ids):
        print(f"-- {id}")