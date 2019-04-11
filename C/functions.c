/* https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number */

/*
 * Copyright (C) 2019  Matthias Paulmier
 *
 * This work is free. You can redistribute it and/or modify it under the
 * terms of the Do What The Fuck You Want To Public License, Version 2,
 * as published by Sam Hocevar. See the COPYING file for more details.
 */

#include <stdio.h>

int
max_of_four (int a, int b, int c, int d)
{
  int max = a;
  if (b > a)
    max = b;
  if (c > max)
    max = c;
  if (d > max)
    max = d;
  return max;
}

int
main ()
{
  int a, b, c, d;
  scanf ("%d %d %d %d", &a, &b, &c, &d);
  int ans = max_of_four (a, b, c, d);
  printf ("%d", ans);

  return 0;
}
