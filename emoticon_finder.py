text = input()
emoticon_list = []

for index in range(len(text)):
    if text[index] == ":":
        emoticon = text[index] + text[index + 1]
        emoticon_list.append(emoticon)
[print(s) for s in emoticon_list]