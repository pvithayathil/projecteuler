def factorial_red(n):
    fact_red = 1
    for i in range(1,(n+1)):
        fact_red = fact_red*i
        if(fact_red % 10 == 0):
            fact_red = fact_red/10
    return fact_red

def sum_digits(n):
    number_str = str(n)
    digit_sum = 0
    for i in number_str:
        digit_sum = digit_sum + int(i)
    return digit_sum
#### similar method not by me:
#reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])
