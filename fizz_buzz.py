#!/usr/bin/python3
from sys import argv
def fizz_buzz(n):
    '''returns fizz for n % 3, buzz for n % 5, and both for both. otherwise returns the number'''
    return 'fizz' * (n % 3 == 0) + 'buzz' * (n % 5 == 0) or n

if __name__ == '__main__':
    print(fizz_buzz(int(argv[1])))