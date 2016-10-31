# euler problem 38

def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

def pe38():
    for n in range(9487, 9213, -1):
        p = str(n*1) + str(n*2)
        if is_pandigital(p): return p
    return "None found."

print pe38()
