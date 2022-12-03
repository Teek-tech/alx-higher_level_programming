#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argv = sys.argv
    arg_length = len(argv) - 1
    a = int(argv[1])
    b = int(argv[3])
    op = sys.argv[2]
    operators = ['+', '-', '*', '/']
    if arg_length != 3:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    if op == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif op == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    else:
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
