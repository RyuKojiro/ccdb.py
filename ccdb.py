#!/usr/bin/env python2.7

import sys
import json
import os.path

path = 'compile_commands.json'

# Setup fp and ccdb objects
if os.path.isfile(path):
    fp = open(path, 'r+')
    ccdb = json.load(fp)
else:
    fp = open(path, 'w')
    ccdb = []

print ccdb
