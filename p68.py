#project euler 68
from itertools import permutations

#initialize all permutations
all_permutations = list(permutations( [1,2,3,4,5,6,7,8,9,10],10))
# ndigit
ndigit = 0

for s in all_permutations:
    if s[0] < s[1] and s[0] < s[2] and s[0] < s[3] and s[0] < s[4]:
        sum1 = s[0] + s[5] + s[6]
        sum2 = s[1] + s[6] + s[7]
        sum3 = s[2] + s[7] + s[8]
        sum4 = s[3] + s[8] + s[9]
        sum5 = s[4] + s[9] + s[5]
        if sum1 == sum2 and sum1 == sum3 and sum1 == sum4 and sum1 == sum5:
            ngon = int(str(s[0]) + str(s[5]) + str(s[6]) +
                       str(s[1]) + str(s[6]) + str(s[7]) +
                       str(s[2]) + str(s[7]) + str(s[8]) +
                       str(s[3]) + str(s[8]) + str(s[9]) +
                       str(s[4]) + str(s[9]) + str(s[5])
                       )
            if ngon > ndigit and len(list(str(ngon))) == 16:
                ndigit = ngon

print ndigit
