#euler problem 48

self_power = 0
for i in range(1,1001):
    power = i
    for j in range(2,i+1):
        power = power*i % 10000000000000
    self_power += power

print self_power % 10000000000
