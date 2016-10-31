#project euler 52

for x in range(1, 1000000):
    x2 = 2*x
    x3 = 3*x
    x4 = 4*x
    x5 = 5*x
    x6 = 6*x
    x_str = list(str(x))
    x2_str = list(str(x2))
    x3_str = list(str(x3))
    x4_str = list(str(x4))
    x5_str = list(str(x5))
    x6_str = list(str(x6))
    x_str.sort()
    x2_str.sort()
    x3_str.sort()
    x4_str.sort()
    x5_str.sort()
    x6_str.sort()
    if (x_str == x2_str and x_str == x3_str and x_str == x4_str and x_str == x5_str and x_str == x6_str):
        print x
        break
    
    
