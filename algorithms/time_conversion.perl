# https://www.hackerrank.com/challenges/time-conversion

# Copyright (C) 2019  Matthias Paulmier

# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.
use strict;
use warnings;

sub timeConversion {
    my ($time) = @_;
    if ($time =~ /^(1[0-2]|0[1-9])(:[0-5][0-9]:[0-5][0-9])([AP]M)$/)
    {
        if ($3 eq 'AM')
        {
            if ($1 == 12) { return "00$2"; }
            return "$1$2";
        }
        my $h = $1 + 12;
        if ($h == 24) { $h = '12'; }
        return "$h$2";

    }
    return 'Not correctly formatted';
}

open(my $fptr, '>', $ENV{'OUTPUT_PATH'});

my $s = <>;
chomp($s);

my $result = timeConversion $s;

print $fptr "$result";

close $fptr;
