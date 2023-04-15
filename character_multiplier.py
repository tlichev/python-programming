def multiplier(str1, str2):
    total_sum = 0
    if len(str1) == len(str2):
        for index in range(0, len(str1)):
            total_sum += ord(str1[index]) * ord(str2[index])
        return total_sum

    elif len(str1) > len(str2):

        for index in range(0, len(str2)):
            total_sum += ord(str1[index]) * ord(str2[index])
        for character in range(len(string2), len(str1)):
            total_sum += ord(str1[character])
        return total_sum

    elif len(str1) < len(str2):

        for index in range(0, len(str1)):
            total_sum += ord(str1[index]) * ord(str2[index])
        for character in range(len(str1), len(str2)):
            total_sum += ord(str2[character])
    return total_sum


strings = input().split()
string1 = strings[0]
string2 = strings[1]
difference = abs(len(string1) - len(string2))
# total_sum = 0
# if len(string1) == len(string2):
#     for index in range(0, len(string1)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#
# elif len(string1) > len(string2):
#     for index in range(0, len(string2)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#     for character in range(len(string2), len(string1)):
#         total_sum += ord(string1[character])
#
# elif len(string1) < len(string2):
#     for index in range(0, len(string1)):
#         total_sum += ord(string1[index]) * ord(string2[index])
#     for character in range(len(string1), len(string2)):
#         total_sum += ord(string2[character])

print(multiplier(string1, string2))
