#euler project 76

# how to sum
def num_sum(n):
    ns = range(1, n)
    ways = [1] + [0]*n

    for i in ns:
        for j in range(i, n+1):
            ways[j] += ways[j-i]
    print ways
    return ways[n]
