/* https://www.hackerrank.com/challenges/reverse-array-c */

/*
 * Copyright (C) 2019  Matthias Paulmier
 *
 * This work is free. You can redistribute it and/or modify it under the
 * terms of the Do What The Fuck You Want To Public License, Version 2,
 * as published by Sam Hocevar. See the COPYING file for more details.
 */

#include <stdio.h>
#include <stdlib.h>

int
main ()
{
  int num, *arr, i;
  scanf ("%d", &num);
  arr = (int *) malloc (num * sizeof (int));
  for (i = 0; i < num; i++)
    {
      scanf ("%d", arr + i);
    }


  /* Write the logic to reverse the array. */

  for (i = 1; i <= num; i++)
    printf ("%d ", *(arr + num - i));
  return 0;
}
