# https://www.hackerrank.com/challenges/finding-the-percentage

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))
    query_name = input()
    total = 0.0
    for score in student_marks[query_name]:
        total += score
    print("{:.2f}".format(total / len(student_marks[query_name])))
