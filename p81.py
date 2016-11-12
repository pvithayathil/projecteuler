#project euler 81
text_file = open('p081_matrix.txt', 'r')
lines = text_file.read().split('\n')
lines = [l.split(",") for l in lines]
lines = lines[0:80]
ori_lines = lines[:]
print lines[0]
y = len(lines[0])
x = len(lines)
for i in xrange(x):
    for j in xrange(y):
        lines[i][j] = int(lines[i][j])

for i in xrange(x):
    for j in xrange(y):
        if i == 0 and j == 0:
            print "the start!"
        elif i * j > 0:
            lines[i][j] += min(lines[i-1][j],lines[i][j-1])
        elif j == 0:
            lines[i][j] += lines[i-1][j]
        elif i == 0:
            lines[i][j] += lines[i][j-1]

        
        
        

print lines[-1][-1]
 
