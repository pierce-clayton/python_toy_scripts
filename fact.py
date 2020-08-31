#!/usr/bin/python3
from sys import argv
def fact(n):
    '''recursive factorial solver up to 998'''
    return n if n < 2 else n * fact(n - 1)

if __name__ == '__main__':
    print(fact(int(argv[1])))

