# https://www.hackerrank.com/challenges/birthday-cake-candles

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input()

    ar = list(map(int, input().rstrip().split()))

    result = ar.count(max(ar))

    fptr.write(str(result) + '\n')

    fptr.close()
