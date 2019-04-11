# https://www.hackerrank.com/challenges/grading

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.


import os
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] > 36:
            if (abs(grades[i] - ((grades[i] // 5) + 1) * 5)) < 3:
                grades[i] = ((grades[i] // 5) + 1) * 5
    return grades


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
