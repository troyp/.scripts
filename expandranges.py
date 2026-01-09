#! /usr/bin/env python

"""Expand a list of numbers including number ranges into a series of individual numbers
eg. expandranges "77, 78, 86, 120-125, 372, 388-390"
The format of the output numbers is determined by the variable separator.
The numbers will be output on individual lines if separator=="\n",
or on a single line separated by commas if separator==", ".
"""

from __future__ import print_function
import sys, re

separator = "\n"
#separator = ", "

def inclusive_range(a, b=None):
    "expand inclusive range a...b, return an iterable of integers"
    if b is None:
        b = a
    return range(int(a), int(b)+1)

def expand_ranges_string(s):
    for term in re.split(r', *', s):
        match = re.match(r'([0-9]+)-([0-9]+)', term)
        if match:
            beg, end = match.groups()
            for i in inclusive_range(beg, end):
                print(i)
        else:
            print(term)

def expand_ranges_string(s):
    res = []
    for term in re.split(r', *', s):
        match = re.match(r'([0-9]+)-([0-9]+)', term)
        if match:
            beg, end = match.groups()
            res.extend((str(n) for n in inclusive_range(beg, end)))
        else:
            res.append(term)
    return res

if __name__ == '__main__':
    s = ''.join(sys.argv[1:])
    print(separator.join(expand_ranges_string(s)))
