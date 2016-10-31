#euler project 57

Expansions = 1000
numerator = 3
denominator = 2
count = 0

for i in range(2, Expansions+1):
    numerator, denominator = numerator + 2*denominator, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
        count += 1

print count
