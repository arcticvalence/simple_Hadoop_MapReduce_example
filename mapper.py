#!/usr/bin/env python
import sys

from sklearn.feature_extraction import stop_words
 
stops = set(stop_words.ENGLISH_STOP_WORDS)

stopwords = set(['the', 'and', 'you', 'that', 'my', 'is', 'not', 'with', 'your', 'have', 'him', 'to', 'of', ',', '.', ':', ';', '!', '?'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
		 print '%s\t%s' % (word, "1")
