#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total_args = len(argv)
    sum = 0
    for i in range(1, total_args):
        sum += int(argv[i])      
    print(sum)
