file = input().split("\\")
file_things = file[-1].split(".")
file_name = file_things[0]
extension = file_things[-1]

print(f'File name: {file_name}')
print(f'File extension: {extension}')
