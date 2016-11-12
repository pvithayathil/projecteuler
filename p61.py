#project euler 61
def cyc_4digit():
    t = 1
    cyc = []
    while t*(t+1)/2 < 10000:
        octa = t*(3*t-2)
        hep = t*(5*t-3)/2
        hexa = t*(2*t-1)
        pent = t*(3*t-1)/2
        square = t*t
        tri = t*(t+1)/2
        if octa >= 1000 and octa < 10000 and octa % 100 > 9:  
            cyc.append((8,octa))
        if hep >= 1000 and hep < 10000 and hep % 100 > 9:
            cyc.append((7,hep))
        if hexa >= 1000 and hexa < 10000 and hexa % 100 > 9:
            cyc.append((6,hexa))
        if pent >= 1000 and pent < 10000 and pent % 100 > 9:
            cyc.append((5,pent))
        if square >= 1000 and square < 10000 and square % 100 > 9:
            cyc.append((4,square)) 
        if tri >= 1000 and tri < 10000 and tri % 100 > 9:
            cyc.append((3,tri))
        t +=1
    return cyc

p = cyc_4digit()
ds = {}
for t1, d1 in p:
    for t2, d2 in p:
        if t1 != t2 and d1 % 100 == d2 // 100:
            ds[t1, d1] = ds.get((t1, d1),[]) + [(t2, d2)] 
        
### see for dictionary implementation: http://blog.dreamshire.com/project-euler-61-solution/
        
def next(types, data):
    if len(types) == 6 and data[0] // 100 == data[-1] % 100:
        print data, sum(data)
    else:
        for t, n in ds.get((types[-1], data[-1]), []):
            if t not in types:
                next(types+[t], data+[n])
print "Project Euler 61 Solution Set"
for type, data in ds: next([type], [data])

