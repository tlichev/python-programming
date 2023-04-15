batch = int(input())
all_batches = 0
cup = 140
single_cookie = 25
small_spoon = 10
big_spoon = 20
cookies_per_box = 5
total_boxes = 0
for _ in range(batch):

    flour = int(input())
    sugar = int(input())
    cocoa = int(input())
    flour_cups = int(flour / cup)
    sugar_spoons = int(sugar / big_spoon)
    cocoa_spoons = int(cocoa / small_spoon)

    total = min(flour_cups, sugar_spoons, cocoa_spoons)
    result = int(((cup + small_spoon + big_spoon) * total) / single_cookie)
    boxes_per_batch = int(result / 5)

    if boxes_per_batch <= 0:
        # print(f"Boxes of cookies: {boxes_per_batch}.")
        print("Ingredients are not enough for a box of cookies.")
    else:
        print(f"Boxes of cookies: {boxes_per_batch}.")
        total_boxes += boxes_per_batch

print(f"Total boxes: {total_boxes}")