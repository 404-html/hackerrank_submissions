# https://www.hackerrank.com/challenges/kangaroo

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import os

def kangaroo(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return 'YES'
    elif x1 == x2 and v1 > v2:
        return 'NO'
    elif x1 <= x2 and v1 <= v2:
        return 'NO'
    elif (x2 - x1) % (v2 - v1) == 0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
