# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4), '\n')

print(formatter % ("one", "two", "three", "four"), '\n')

print(formatter % (True, False, True, False), '\n')

print(formatter % (formatter, formatter, formatter, formatter), '\n')

print(formatter %
      (
          "I had this thing.",
          "That you could type up right.",
          "But it didn't sing.",
          "So I said goodnight."
      )
      )
