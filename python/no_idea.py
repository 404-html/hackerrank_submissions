# https://www.hackerrank.com/challenges/no-idea

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

happiness = 0
if __name__ == "__main__":
    (lenA, lenB) = input().split(" ")
    arr = input().split()
    A = set(input().split())
    B = set(input().split())
    print (sum([(i in A) - (i in B) for i in arr]))
