# -*- coding: utf-8 -*-

# python ex17.py ex15_sample.txt ex17_sample.txt

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copy from %s to %s" % (from_file, to_file))

input_f = open(from_file)

indata = input_f.read()

# indata = open(from_file).read()

print("The input file is %d bytes long." % len(indata))

print("Does the output file exist? %r" % exists(to_file))

print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

output_f = open(to_file, 'w')

output_f.write(indata)

print("Alright, all done.")

output_f.close()

input_f.close()

# open(from_file).close
