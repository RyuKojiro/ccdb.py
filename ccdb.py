#!/usr/bin/env python2.7

import sys
import json
import os
from subprocess import call

# Constants
path = 'compile_commands.json'
actualCCKey = 'ACTUAL_CC'

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

# Pass through to the compiler
newCommand = sys.argv

if actualCCKey in os.environ:
    actualCC = os.environ[actualCCKey]
else:
    # The safest assumption is just 'cc'
    actualCC = 'cc'

newCommand[0] = actualCC

call(newCommand)
