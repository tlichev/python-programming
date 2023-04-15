country_names = input().split(", ")
capital_names = input().split(", ")

res = dict(zip(country_names, capital_names))
for k, v in res.items():
    print(f"{k} -> {v}")