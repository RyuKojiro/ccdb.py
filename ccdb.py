#!/usr/bin/env python2.7

import sys
import json
import os
from subprocess import call

languages = [".m", ".c", ".cpp", ".cc", ".mm", ".cxx"]
def FileForInvocation(argv):
    for arg in argv:
        for ext in languages:
            if arg.endswith(ext):
                return arg

# Constants
path = 'compile_commands.json'
actualCCKey = 'ACTUAL_CC'

# Setup ccdb object by reading in old JSON or initializing
if os.path.isfile(path):
    fp = open(path, 'r')
    ccdb = json.load(fp)
    fp.close()
else:
    ccdb = []

# Change command to reflect what would actually go to the compiler
command = sys.argv

if actualCCKey in os.environ:
    actualCC = os.environ[actualCCKey]
else:
    actualCC = 'cc' # The safest assumption is just 'cc'

command[0] = actualCC

# Append current command to database
cwd = os.getcwd()
this = dict([('directory', cwd), ('command', ' '.join(command)), ('file', FileForInvocation(command))])
ccdb.append(this)

# Write out updated JSON
print 'Compilation database "' + cwd + '/' + path + '" appended.'
fp = open(path, 'w')
json.dump(ccdb, fp)
fp.close()

# Pass through to the compiler
call(command)
