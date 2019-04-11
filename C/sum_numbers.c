/* https://www.hackerrank.com/challenges/sum-numbers-c */

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
  char ch;
  char s[512];
  char sentence[512];
  scanf ("%c%*c", &ch);
  scanf ("%s%*c", &s);
  scanf ("%[^\n]%*c", &sentence);
  printf ("%c\n%s\n%s\n", ch, &s, &sentence);
  return 0;
}
