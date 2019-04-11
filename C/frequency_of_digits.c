/* https://www.hackerrank.com/challenges/frequency-of-digits-1 */

/*
 * Copyright (C) 2019  Matthias Paulmier
 *
 * This work is free. You can redistribute it and/or modify it under the
 * terms of the Do What The Fuck You Want To Public License, Version 2,
 * as published by Sam Hocevar. See the COPYING file for more details.
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int
main (void)
{
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  char *s = malloc (1024 * sizeof (char));
  scanf ("%s", s);
  int nums[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
  for (int i = 0; i < strlen (s); i++)
    if (*(s + i) <= '9' && *(s + i) >= '0')
      ++nums[*(s + i) - '0'];
  for (int i = 0; i < 10; i++)
    printf ("%d ", nums[i]);
  printf ("\n");
  return 0;
}
