# euler problem 45

def is_pentagonal(x):
    p = ((24*x + 1)**.5+ 1.0)/6.0
    return p == int(p)

done = 0
i = 143
while done == 0:
    i += 1
    r = i*(2*i-1)
    if is_pentagonal(r):
        print r
        done = 1
        break
