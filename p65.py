#project euler 65

# numerator is n(i) = cf(i)*n(i-1) + n(i-2)

n0 = 1
n1 = 2
cf_end =100

for i in xrange(2, cf_end+1):
    cfi = 1 if i % 3 else 2 *i//3
    n0, n1 = n1, n0 + n1 * cfi

print sum(map(int, str(n1)))
