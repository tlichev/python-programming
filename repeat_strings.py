text = input().split()
output_text = []

for w in text:
    length = len(w)
    output_text.append(w*length)

print("".join(output_text))
