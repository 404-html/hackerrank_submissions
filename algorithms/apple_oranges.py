# https://www.hackerrank.com/challenges/apple-and-orange

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount, orangecount = 0, 0
    for apple in apples:
        if (apple + a) in range(s, t+1):
            applecount +=1
    for orange in oranges:
        if (orange + b) in range(s, t+1):
            orangecount += 1
            print('{}\n{}'.format(applecount, orangecount))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
