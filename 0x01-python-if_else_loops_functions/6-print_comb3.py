#!/usr/bin/python3
unique_num = 0
while unique_num <= 89:
    if unique_num % 10 == 0:
        unique_num += 1 + unique_num // 10
    print("{:02d}".format(unique_num), end='\n' if unique_num == 89 else ", ")
    unique_num += 1
