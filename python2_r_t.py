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
        print"%-25s \033[0;32mMATCHED\033[0m" % (pattern) # if match
    else:
        print"%-25s \033[0;31mMATCHED\033[0m" % (pattern) # if not matched
