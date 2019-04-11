/* https://www.hackerrank.com/challenges/sum-of-digits-of-a-five-digit-number */

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
  int res =
    n % 10 + (n % 100) / 10 + (n % 1000) / 100 + (n % 10000) / 1000 +
    n / 10000;
  printf ("%d", res);
  //Complete the code to calculate the sum of the five digits on n.
  return 0;
}
