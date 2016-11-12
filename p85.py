# project euler 85

# number of subrectangles in m x n grid is:
# m*(m+1)*n(n+1)/4
target = 2000000.0
near_tar = 2000000.0
n = 3.0
ab = n * (n+1)
m = int((-ab + (ab**2 - 4 * ab * -1 * 4 * target)**.5)/(2*ab))
    
while n < m:
    
    if abs(4 * target - m*(m+1)*n*(n+1)) < abs(4 * target - (m+1)*(m+2)*n*(n+1)):
        if abs(4 * target - m*(m+1)*n*(n+1)) < near_tar:
            near_tar = abs(4 * target - m*(m+1)*n*(n+1))
            area = m*n
    else:
        if abs(4 * target - (m+1)*(m+2)*n*(n+1)) < near_tar:
            near_tar = abs(4 * target - (m+1)*(m+2)*n*(n+1))
            area = (m+1)*n
    n += 1
    ab = n * (n+1)
    m = int((-ab + (ab**2 - 4 * ab * -1 * 4 * target)**.5)/(2*ab))
                           
    
print area
