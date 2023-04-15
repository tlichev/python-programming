banned_words = input().split(", ")
text = input()

for w in banned_words:
    length = len(w)
    text = text.replace(w, "*" * length)

print(text)
