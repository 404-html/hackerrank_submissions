/* https://www.hackerrank.com/challenges/1d-arrays-in-c */

/*
 * Copyright (C) 2019  Matthias Paulmier
 *
 * This work is free. You can redistribute it and/or modify it under the
 * terms of the Do What The Fuck You Want To Public License, Version 2,
 * as published by Sam Hocevar. See the COPYING file for more details.
 */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int
main ()
{
  int n;
  scanf ("%d", &n);
  int res = 0;
  for (int i = 0; i < n; i++)
    {
      int _scan;
      scanf ("%d", &_scan);
      res += _scan;
    }
  printf ("%d\n", res);
  return 0;
}
