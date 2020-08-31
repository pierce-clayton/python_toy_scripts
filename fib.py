#!/usr/bin/python3
from sys import argv
from functools import lru_cache
@lru_cache(maxsize=256)
def fib(n):
    '''returns fib the lazy way with the standard library providing memoization up to 499'''
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib(int(argv[1])))