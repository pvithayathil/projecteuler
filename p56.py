#euler problem 56

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

max_digit_sum = 0
for a in range(2,100):
    for b in range(2,100):
        t_sum = sum_digits(a**b)
        if t_sum > max_digit_sum:
            max_digit_sum = t_sum

print max_digit_sum
