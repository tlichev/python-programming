import sys

divisor = int(input())
boundary = int(input())
max_num = -sys.maxsize
for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > max_num:
            max_num = i
print(max_num)