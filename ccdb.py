#!/usr/bin/env python2.7

import sys
import json
import os
from subprocess import call
import fcntl

languages = [".m", ".c", ".cpp", ".cc", ".mm", ".cxx"]
def FileForInvocation(argv):
    for arg in argv:
        for ext in languages:
            if arg.endswith(ext):
                return arg

# Constants
path = 'compile_commands.json'
actualCCKey = 'ACTUAL_CC'

# Open and lock the file
fp = open(path, 'w+')
fcntl.flock(fp, fcntl.LOCK_EX)

# Setup ccdb object by reading in old JSON or initializing
try:
    ccdb = json.load(fp)
    fp.seek(0, 0)
except:
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
json.dump(ccdb, fp)

# Unlock and cleanup
fp.flush()
fcntl.flock(fp, fcntl.LOCK_UN)
fp.close()

# Pass through to the compiler so that the build will actually succeed
call(command)
