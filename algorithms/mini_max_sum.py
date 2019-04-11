# https://www.hackerrank.com/challenges/mini-max-sum

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

def getMinMaxSum(arr):
    arr.sort()
    return (sum(arr[0:-1]), sum(arr[1:]))

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min, max = getMinMaxSum(arr)
    print('%d %d' % (min, max))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
