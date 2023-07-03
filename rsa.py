#!/usr/bin/python3
'''
My Factorization module
'''
import sys
import math


def is_prime(n):
    '''
    Checks if a number is a prime number

    Arguments
    -------
    n : int
        Number to check

    Returns
    -------
    bool
        True if the number is prime, False otherwise
    '''
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def rsa(n):
    '''
    find 2 prime factors for a number(n)

    Arguments
    -------
    n : int
        number that to which the 2 prime factors are obtained!
    '''
    if n < 2:
        return
    x = None
    for i in range(2, math.isqrt(n) + 1):
        if not (n % i) and is_prime(i):
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
    '''
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return
    file_name = sys.argv[1]
    try:
        with open(file_name, 'r') as file:
            for line in file:
                num = int(line.strip())
                rsa(num)
    except FileNotFoundError:
        print(f"File {file_name} not found!")


if __name__ == '__main__':
    read_file()
