#!/usr/bin/env python2.7

import sys
import json
import os

path = 'compile_commands.json'

# Setup fp and ccdb objects
if os.path.isfile(path):
    fp = open(path, 'r+')
    ccdb = json.load(fp)
else:
    fp = open(path, 'w')
    ccdb = []

# Append current command
this = dict([('directory', os.getcwd()), ('command', str(sys.argv)), ('file', sys.argv[-1])])
ccdb.append(this)

# Write out
print ccdb
json.write(ccdb, fp)
fp.close()
