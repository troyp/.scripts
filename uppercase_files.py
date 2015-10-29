#!/usr/bin/python

from __future__ import print_function
import os

files = os.listdir('.')
with open('.upcase_files_folders.log','a') as logfile:
    for f in files:
        newname = f.upper()
        if f == '.upcase_files_folders.log' or newname == f:
            continue
        if newname in files :
            print( "error: %s already exists: file %s not renamed" % (newname, f) )
            continue
        os.rename(f, newname)
        print( "renamed:  %s  -->  %s" % (repr(f), repr(newname)), file = logfile )
