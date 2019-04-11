/* https://www.hackerrank.com/challenges/bitwise-operators-in-c */

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
//Complete the following function.


void
calculate_the_maximum (int n, int k)
{
  int max_or = 0, max_and = 0, max_xor = 0;
  for (int a = 1; a < n; a++)
    {
      for (int b = a + 1; b <= n; b++)
	{
	  if ((a ^ b) > max_xor && (a ^ b) < k)
	    max_xor = a ^ b;
	  if ((a | b) > max_or && (a | b) < k)
	    max_or = a | b;
	  if ((a & b) > max_and && (a & b) < k)
	    max_and = a & b;
	}
    }
  printf ("%d\n%d\n%d\n", max_and, max_or, max_xor);
}

int
main ()
{
  int n, k;

  scanf ("%d %d", &n, &k);
  calculate_the_maximum (n, k);

  return 0;
}
