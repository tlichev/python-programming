items = input().split()
junk_items = {}
flag = False
legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
while flag == False:
    for index in range(1, len(items), 2):
        item = items[index].lower()
        value = int(items[index - 1])
        if item in legendary_items:
            legendary_items[item] += value
            if legendary_items[item] >= 250:
                legendary_items[item] -= 250
                if item == "shards":
                    print("Shadowmourse obtained!")
                    flag = True
                    break
                elif item == "fragments":
                    print("Valanyr obtained!")
                    flag = True
                    break
                elif item == "motes":
                    print("Dragonwrath obtained!")
                    flag = True
                    break


        else:
            if item not in junk_items:
                junk_items[item] = value
            else:
                junk_items[item] += value
    if flag == True:
        break
    items = input().split()


sorted_legendary_items = sorted(legendary_items.items(), key=lambda x: (-x[1], x[0]))
sorted_junk_items = sorted(junk_items.items(), key=lambda x: x[0])

for k, v in sorted_legendary_items:
    print(f"{k}: {v}")
for k, v in sorted_junk_items:
    print(f"{k}: {v}")
