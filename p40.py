#p40
d = [0]
for i in range(1,1000000):
    d.extend(list(str(i)))


print int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])
