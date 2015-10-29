#!/usr/bin/python

from __future__ import print_function
import os

with open('.upcase_files_folders.log','a') as logfile:
    renames = []
    for d, subdirs, fs in os.walk(os.getcwd()):
        for x in fs + subdirs:
            oldname = os.path.join(d, x)
            newname = os.path.join(d, x.upper())
            if x == '.upcase_files_folders.log' or newname == oldname:
                continue
    for (oldname, newname) in reversed(renames):
        os.rename(oldname, newname)
        print( "renamed:  %s  -->  %s" % (repr(oldname), repr(newname)), file = logfile )
