#!/usr/bin/python3

"""Expands lines from an index containing an entry followed by a list of pages
(which may contain page ranges). This script reformats the entries for use
(after conversion) in a PDF table of contents, with each page on a separate
line. The first page from an entry is listed after the entry text; further
pages are indented and may replace the entry text with continuation text.

Parameters:
  continuation: this string is used in place of the entry text for subsequent
  pages. To use the entry text for all pages, set continuation = False
  indent: this string is the additional indentation added to subsequent page
  entries
  expand_ranges_p: Takes the value True or False. If True, page ranges are
  expanded and each individual page listed (this may be a lot of pages). If
  False, only the first page of a range is included.
"""

import sys, re

# PARAMETERS: Default values
continuation = "also…"
indent = "  "
expand_ranges_p = False

# PARAMETERS: User set - uncomment and add desired value
# continuation = 
# indent = 
# expand_ranges_p = 

def inclusive_range(a, b=None):
    "expand inclusive range a...b, return an iterable of integers"
    if b is None:
        b = a
    return range(int(a), int(b)+1)

def expand_ranges_string(s):
    res = []
    for term in re.split(r', *', s):
        match = re.match(r'([0-9]+)-([0-9]+)', term)
        if match:
            beg, end = match.groups()
            if expand_ranges_p:
                res.extend((str(n) for n in inclusive_range(beg, end)))
            else:
                res.append(beg)
        else:
            res.append(term)
    return res

def process_line(line):
    page_expr_match = re.match(r'^(\s*)(.*[^-0-9, ]) ([-0-9, ]+$)', line)
    if page_expr_match:
        ws, entry, page_expr = page_expr_match.groups()
        pages = expand_ranges_string(page_expr)
        print("%s%s %s"%(ws, entry, pages[0]))
        for page in pages[1:]:
            print("%s%s%s %s"%(ws, indent, continuation, page))
    else:
        print(line)

if __name__ == '__main__':
    for line in sys.stdin:
        line.rstrip()
        process_line(line)

