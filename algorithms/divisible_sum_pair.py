# https://www.hackerrank.com/challenges/divisible-sum-pairs

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(k, ar):
    total = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                total += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().split()[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
