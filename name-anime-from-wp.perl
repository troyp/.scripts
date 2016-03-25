#! /usr/bin/env perl

# converts anime episode list CSV (generated using .pentadactylrc command `table2csv`)
# into a list of file names in format:  `number - english ・ romaji (japanese)`
    
my $usage = "Usage: name-anime-from-wp [OPTION...] [FILE]

    -h\tShow this help text
    -d\tStrip descriptions from file (only process odd lines)\n";

my $odd_only = 0;

while ( $ARGV[0] =~ "^-" ) {
    if ( "$ARGV[0]" =~ /^--?h(elp)?$/ ) {
        print "$usage";
        exit;
    }
    if ( "$ARGV[0]" =~ /^--?(d|remove-descriptions)$/ ) {
        $odd_only = 1;
        shift;
    }
}

my $f = @ARGV>0 ? $ARGV[0] : '-';

open IN, "< $f" or die "$0: open $f failed, code $!\n";
while ( defined ($_=<IN>) ) {
    unless ( $odd_only && $. % 2 ) {
        s/"(\d+)","""([^"]+)" (?:"([^"]+)"([^"]+) ")?.*/$1 - $2 ・ $3$4/;
        # if string ends in " ・ " (ie. no japanese name), delete the " ・ ".
        # note: \xe3\x83\xbb is "・" as an 8-bit string.
        s/ \xe3\x83\xbb $//;
        print;
    }
}

close IN or die "$0: close $f failed, code $!\n";
