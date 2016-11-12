# project euler 63
from math import log10
####
count = 0
for n in range(1, 10):
    count += int(1 / (1 - log10(n)))

print count
