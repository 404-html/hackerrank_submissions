# https://www.hackerrank.com/challenges/the-birthday-bar

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os


def birthday(s, d, m):
    if len(s) == 1 and s[0] == d and m == 1:
        return 1
    ways = 0
    for i in range((len(s) - m) + 1):
        if sum(s[i:i+m]) == d:
            ways += 1
    return ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
