#p29

L = 100
r = range(2, L+1)

print len({a**b for a in r for b in r})
