#Euler 33
from fractions import gcd

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician
#in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
#is correct, is obtained by cancelling the 9s. We shall consider fractions like,
#30/50 = 3/5, to be trivial examples.There are exactly four non-trivial examples
#of this type of fraction, less than one in value, and containing two digits in
#the numerator and denominator.If the product of these four fractions is given
#in its lowest common terms, find the value of the denominator.

def digit():
    digit = []
    for i in range(11,99):
        num = list(str(i))
        for j in range(i+1,100):
            fract = float(i)/ j
            dem = list(str(j))
            if num[1] == dem[0] and int(dem[1]) != 0:
                fract2 = float(int(num[0]))/int(dem[1])
                if fract == fract2:
                    digit.append([i,j])
            elif num[1] == dem[1] and int(dem[0]) != 0:
                fract2 == float(int(num[0]))/int(dem[0])
                if fract == fract2:
                    digit.append([i,j])
            elif num[0] == dem[0] and int(dem[1]) != 0:
                fract2 == float(int(num[1]))/int(dem[1])
                if fract == fract2:
                    digit.append([i,j])
            elif num[0] == dem[1] and int(dem[0]) != 0:
                fract2 = float(int(num[1]))/int(dem[0])
                if fract == fract2:
                    digit.append([i,j])
    n = 1
    d = 1
    for i in digit:
        n = n*i[0]
        d = d*i[1]
    g = gcd(n,d)
    
    return d/g
