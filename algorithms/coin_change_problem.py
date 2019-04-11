# https://www.hackerrank.com/challenges/coin-change

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

def count_parts(val, coins, idx=0, memo=None):
    ''' Enumarate the partitions
    Their is a small optimisation that memorizes the subproblems already solved
    '''
    if memo is None:
        memo = dict()

    if val == 0:
        return 1

    if idx >= len(coins):
        return 0

    key = "{}_{}".format(str(val), str(idx))
    if key in memo.keys():
        return memo[key]

    total = 0
    ways = 0
    while total <= val:
        rest = val - total
        ways += count_parts(rest, coins, idx+1, memo)
        total += coins[idx]
    memo[key] = ways
    return ways

if __name__ == "__main__":
    n,m = map(int, input().split())
    coins = list(map(int, input().split()))
    print(count_parts(n, coins))
