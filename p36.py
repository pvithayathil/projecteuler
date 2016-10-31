#p36

def pal(x):
    pal_list = []
    for i in range(1,x):
        binary =int(bin(i)[2:])
        if(is_pal(binary) == 1 and is_pal(i) == 1):
            pal_list.append(i)
    return pal_list

def is_pal(x):
    is_pal_list = list(str(x))
    is_pal_len = len(is_pal_list)
    for i in range(0,is_pal_len/2):
        if int(is_pal_list[i]) != int(is_pal_list[is_pal_len - i - 1]):
            return 0
    return 1
