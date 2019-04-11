# https://www.hackerrank.com/challenges/write-a-function

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

 year = int(input())
 print(is_leap(year))
