# https://www.hackerrank.com/challenges/simple-array-sum/submissions/code/93311740

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

if __name__ == '__main__':
    _ = int(input())

    print(sum(list(map(int, input().rstrip().split()))))
