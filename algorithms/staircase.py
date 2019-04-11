# https://www.hackerrank.com/challenges/staircase

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for _ in range(n-1-i):
            print(' ', end='')
        for _ in range(n-1-i,n):
            print('#', end='')
            print('')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
