# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maxi = -100
    ru = -101
    for i in arr:
        if i > maxi:
            ru = maxi
            maxi = i
        if i > ru and i != maxi:
            ru = i
    print(ru)
