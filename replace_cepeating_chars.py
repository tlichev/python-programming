text = input()
last_ch = ""
output_text = ""
for ch in text:

    if last_ch != ch:
        output_text += ch
    last_ch = ch
print(output_text)
