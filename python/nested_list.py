# https://www.hackerrank.com/challenges/nested-list

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        students.append([input(), float(input())])
    second_highest = sorted(list(set([mark for _, mark in students])))[1]
    print("\n".join(sorted([name for name, mark in students if mark == second_highest])))
