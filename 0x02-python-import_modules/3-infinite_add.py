#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_args = len(sys.argv)
    sum = 0
    for i in range(1, total_args):
        sum += int(sys.argv[i])      
    print(sum)
