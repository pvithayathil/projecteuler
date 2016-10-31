#euler project 99
from math import log

### read text file
text_file = open('p099_base_exp.txt', 'r')
lines = text_file.read().split('\n')
mv, ml = 0, 0 

for ln, line in enumerate(lines, start=1):
    b, e = line.split(',') 
    v = int(e) * log(int(b)) 
    if v > mv: 
        mv, ml = v, ln 

print ml
