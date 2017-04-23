#!/usr/bin/env python2.7

import sys
import json
import os

path = 'compile_commands.json'

# Setup ccdb object
if os.path.isfile(path):
    fp = open(path, 'r')
    ccdb = json.load(fp)
    fp.close()
else:
    ccdb = []

# Append current command
cwd = os.getcwd()
this = dict([('directory', cwd), ('command', str(sys.argv)), ('file', sys.argv[-1])])
ccdb.append(this)

# Write out
print 'Compilation database "' + cwd + '/' + path + '" appended.'
fp = open(path, 'w')
json.dump(ccdb, fp)
fp.close()
