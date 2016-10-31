#euler problem 55

def is_palindrome(n):
    if (str(n) == str(n)[::-1]):
        return 1
    else:
        return 0

not_ly = 0
for i in range(1,10001):
    for j in range(1,50):
        i = i + int(str(i)[::-1])
        if is_palindrome(i) == 1:
            not_ly +=1
            break

print 10000 - not_ly
