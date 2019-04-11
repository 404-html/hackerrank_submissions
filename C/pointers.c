/* https://www.hackerrank.com/challenges/pointer-in-c */

/*
 * Copyright (C) 2019  Matthias Paulmier
 *
 * This work is free. You can redistribute it and/or modify it under the
 * terms of the Do What The Fuck You Want To Public License, Version 2,
 * as published by Sam Hocevar. See the COPYING file for more details.
 */

#include <stdio.h>
#include <math.h>

void
update (int *a, int *b)
{
  // Complete this function
  int _a = *a;
  (*a) = _a + *b;
  (*b) = abs (_a - *b);
}

int
main ()
{
  int a, b;
  int *pa = &a, *pb = &b;

  scanf ("%d %d", &a, &b);
  update (pa, pb);
  printf ("%d\n%d", a, b);

  return 0;
}
