import re
text = input()

matches_nums = re.findall(r"\d", text)
cool_threshold = 1
for num in matches_nums:
    cool_threshold *= int(num)


print(f"Cool threshold: {cool_threshold}")


pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
matches = re.finditer(pattern, text)
cool_emojis = []
emojis_count = 0
for match in matches:
    emoji = match.group()
    emoji_without_surrounding = emoji.replace(emoji[0], "")
    emoji_coolness = sum([ord(el) for el in emoji_without_surrounding])
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji)

    emojis_count += 1


print(f"{emojis_count} emojis found in the text. The cool ones are:")
for e in cool_emojis:
    print(e)



