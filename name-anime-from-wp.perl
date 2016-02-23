#! /usr/bin/env perl

# converts anime episode list CSV (generated using .pentadactylrc command `table2csv`)
# into a list of file names in format:  `number - english ・ romaji (japanese)`
    
my $f = @ARGV>0 ? $ARGV[0] : '-';

open IN, "< $f" or die "$0: open $f failed, code $!\n";
while ( defined ($_=<IN>) ) {
    unless ( $. % 2 ) {
        s/"(\d+)","""([^"]+)" "([^"]+)"([^"]+) ".*/$1 - $2 ・ $3$4/;
        print;
    }
}
close IN or die "$0: close $f failed, code $!\n";
