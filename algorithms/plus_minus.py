# https://www.hackerrank.com/challenges/plus-minus

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

def plusMinus(arr):
    totals = [0,0,0]
    for i in arr:
        if i > 0:
            totals[0] += 1
        elif i < 0:
            totals[1] += 1
        else:
            totals[2] += 1
    return totals

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    totals = plusMinus(arr)
    for t in totals:
        print('%.6f' % (t / len(arr)))
