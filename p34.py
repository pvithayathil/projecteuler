#p34
import math as m
# digit factorials
a = [0,1,2,3,4,5,6,7,8,9]
b = [m.factorial(0),m.factorial(1),m.factorial(2),m.factorial(3),m.factorial(4),m.factorial(5),m.factorial(6),m.factorial(7),m.factorial(8),m.factorial(9)]

digit_fact = []
for i in range(3,999999):
    num = list(str(i))
    digit_sum = 0
    for n in num:
        digit_sum += b[int(n)]

    if digit_sum == i:
        digit_fact.append(i)

