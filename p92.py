#euler project 92

def is_square_digit_89(n):
    if n == 1:
        return 0
    elif n == 89:
        return 1
    else:
        str_n = str(n)
        squared = 0
        for i in str_n:
            squared += int(i)**2
        return is_square_digit_89(squared)

count_89 = 0
for i in range(1,10000000):
    count_89 += is_square_digit_89(i)
