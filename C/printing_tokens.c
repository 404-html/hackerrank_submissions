/* https://www.hackerrank.com/challenges/printing-tokens- */

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
  char *s;
  s = malloc (1024 * sizeof (char));
  scanf ("%[^\n]", s);
  s = realloc (s, strlen (s) + 1);

  for (int i = 0; i < strlen (s); i++)
    if (*(s + i) != ' ')
      printf ("%c", *(s + i));
    else
      printf ("\n");
  return 0;
}
