# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

def breakingRecords(scores):
    max_b, min_b = 0, 0
    prev_max = prev_min = scores[0]
    for s in scores[1:]:
        print(s)
        if s > prev_max:
            prev_max = s
            max_b += 1
        if s < prev_min:
            prev_min = s
            min_b += 1
    return max_b, min_b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
