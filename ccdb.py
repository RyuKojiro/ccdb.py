#!/usr/bin/env python2.7

import sys
import json
import os.path

path = 'compile_commands.json'

if os.path.isfile(path):
    f = open(path, 'r+')
    ccdb = json.load(f)

print ccdb
