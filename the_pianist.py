num = int(input())
dict_pieces = {}
for _ in range(num):
    data = input().split("|")
    piece = data[0]
    composer = data[1]
    key = data[-1]
    dict_pieces[piece] = []
    dict_pieces[piece].append(composer)
    dict_pieces[piece].append(key)
# print(dict_pieces)

command = input().split("|")
while command[0] != "Stop":
    if command[0] == "Add":
        piece_command = command[1]
        composer_command = command[2]
        key_command = command[-1]
        if piece_command not in dict_pieces:
            dict_pieces[piece_command] = []
            dict_pieces[piece_command].append(composer_command)
            dict_pieces[piece_command].append(key_command)
            print(f"{piece_command} by {composer_command} in {key_command} added to the collection!")
        else:
            print(f"{piece_command} is already in the collection!")
    elif command[0] == "Remove":
        piece_command = command[1]
        if piece_command in dict_pieces:
            del dict_pieces[piece_command]
            print(f"Successfully removed {piece_command}!")
        else:
            print(f"Invalid operation! {piece_command} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        piece_command = command[1]
        key_command = command[-1]
        if piece_command in dict_pieces:
            dict_pieces[piece_command][1] = key_command
            print(f"Changed the key of {piece_command} to {key_command}!")
        else:
            print(f"Invalid operation! {piece_command} does not exist in the collection.")
    command = input().split("|")


dict_pieces = sorted(dict_pieces.items(), key=lambda x: x[0])
for piece, data in dict_pieces:
    print(f"{piece} -> Composer: {data[0]}, Key: {data[1]}")