__author__ = 'grokrz'

v1 = [1, 3, 2, 1, 2, 1, 1]

v2 = [7, 0, 2, 1, 0, 0, 1]
v3 = [1, 7, 0, 0, 2, 0, 1]
v4 = [1, 0, 0, 0, 7, 1, 2]
v5 = [0, 2, 0, 0, 7, 1, 1]


def check(org, vectors):
    for v in vectors:
        print("Computing: ", org, v)
        i = 0
        result = 0
        for o1 in org:
            result += o1 * v[i]
            i += 1
        print("Sum", result)


check(v1, [v2, v3, v4, v5])

words = ['the', 'on', ' and', 'go', 'round', 'bus', 'wheels']

sentence = 'the wheels on the bus go round and round.'

from collections import Counter
import re

w = re.findall(r'\w+', sentence)
c = Counter(w)
print c

for word in words:
    print c[word]
