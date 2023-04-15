letters = input().split(", ")
ascii_letters = {word: ord(word) for word in letters }
print(ascii_letters)
