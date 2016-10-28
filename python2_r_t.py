#! /usr/bin/python

import re

# get regex from file
with open('./regex', 'r') as myfile:
    regex=myfile.read().replace('\n', '')

# compile regex
my_test = re.compile(regex)

print"""
Testing the following python2 regex
================================
\v%s\v
================================""" % regex

# get patterns to test from file
with open('./patterns', 'r') as myfile:
    patterns=myfile.read().splitlines() 

# test regex
for pattern in patterns:
    if my_test.search(pattern):
        print"\033[0;32m%-6s\033[0m %s" % ("MATCH", pattern) # if match
    else:
        print"\033[0;31m%-6s\033[0m %s" % ("FAIL", pattern) # if not matched

