def fib_1000():
    f1 = 1
    f2 = 1
    fib_seq = 2
    while len(str(f2)) < 1000:
        f_hold = f2
        f2 = f2 + f1
        f1 = f_hold
        fib_seq += 1

    print fib_seq

fib_1000()
