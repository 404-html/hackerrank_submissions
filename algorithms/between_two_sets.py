# https://www.hackerrank.com/challenges/between-two-sets

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

def getTotalX(a, b):
    a.sort()
    b.sort()
    a_factors = set()
    for i in range(a[-1], b[0] + 1):
        test_factor = True
        for j in a:
            if i % j != 0:
                test_factor = False
                break
        if test_factor: a_factors.add(i)
    b_factors = set()
    for y in a_factors:
        test_factor = True
        for x in b:
            if x % y != 0:
                test_factor = False
                break
        if test_factor: b_factors.add(y)
    return len(b_factors)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
