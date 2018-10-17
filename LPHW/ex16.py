# -*- coding: utf-8 -*-

# python ex16.py ex16_sample.txt

# I need to shave it off.
# I say I don't like my hair.
# To all the people out there.


from sys import argv

script, filename = argv

print("We're going to erase %r" % filename)

print("If you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit RETURN.")

input("?")


print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1 : ")

line2 = input("Line 2 : ")

line3 = input("Line 3 : ")

all_lines = line1 + '\n' + line2 + '\n' + line3

# print (all_lines)

print("I'm going to write there to the file.")

target.write(all_lines)

print("And finally. we close it.")

target.close()
