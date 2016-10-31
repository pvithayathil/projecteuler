
def diag_sum(n):
    if n == 1:
        return 1
    else:
        square = n*n
        return 4*square - (n-1) - 2*(n-1) - 3*(n-1) + diag_sum(n-2)
