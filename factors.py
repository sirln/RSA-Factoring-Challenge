#!/usr/bin/python3
'''
My Factorization module
'''
import sys
import math


def factorize(n):
    '''
    factorizes a number into a product of 2 smaller numbers

    Arguments
    -------
    n : int
        number to be factorized
    '''
    if n < 2:
        return
    x = None
    for i in range(2, math.isqrt(n) + 1):
        if not (n % i):
            x = i
            break
    if x is not None:
        y = n // x
        print(f"{n}={y}*{x}")


def read_file():
    '''
    reads a file passed into the program

    Raises
    ------
    FileNotFoundError
        if file passed as argument 1 is not available / not found.
    ValueError
        if value/number in line is not a valid integer value.
    '''
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    num = int(line.strip())
                    factorize(num)
                except ValueError:
                    print(f"Invalid input in file: {line.strip()}")
    except FileNotFoundError:
        print(f"File {file_name} not found!")


if __name__ == '__main__':
    read_file()
