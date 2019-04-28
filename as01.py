# Python set-based spell checker
# Uses python sets and dictionary files to run a spell check on given text.

import re
import fileinput
words = set()
dictionary = set()

for line in fileinput.input(files=('/usr/share/dict/american-english-insane',
                                   '/usr/share/dict/british-english-insane',
                                   '/srv/datasets/scrabble-CSW12-words.txt')):
  for word in line.split():
    dictionary.add(word.lower())

for line in fileinput.input():
  lineList = re.sub(r"[^A-z']+", " ", line).lower().split()
  for item in lineList:
    words.add(item.strip("'"))

for item in sorted(words):
  if item not in dictionary:
    print(item)
