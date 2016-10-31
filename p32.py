import itertools

pan = list(itertools.permutations([1,2,3,4,5,6,7,8,9],9))

pan = [1,2,3,4,5,6,7,8,9]

def case144(pan_list):
    pan_product = []
    for p in pan_list:
        t_pan = pan_list[:]
        t_pan.remove(p)
        list4 = list(itertools.permutations(t_pan,4))
        for i in list4:
            t_pan2 = t_pan[:]
            multiplier_list = list(i)
            multiplier = multiplier_list[0]*1000 + multiplier_list[1]*100 + multiplier_list[2]*10 + multiplier_list[3]*1
            product = p*multiplier
            product_list = list(str(product))
            product_list.sort()
            for j in multiplier_list:
                t_pan2.remove(j)
            t_pan2.sort()
            a = t_pan2[0]*1000 + t_pan2[1]*100 + t_pan2[2]*10 + t_pan2[3]*1
            b = int(product_list[0])*1000 + int(product_list[1])*100 + int(product_list[2])*10 + int(product_list[3])
            if a == b:
                pan_product.append(product)
    return pan_product
        
def case234(pan_list):
    pan_product = []
    list2 = list(itertools.permutations(pan_list,2))
    for l in list2:
        m = list(l)
        mult = m[0]*10+m[1]
        t_pan = pan_list[:]
        t_pan.remove(m[0])
        t_pan.remove(m[1])
        list3 = list(itertools.permutations(t_pan,3))
        for i in list3:
            t_pan2 = t_pan[:]
            multiplier_list = list(i)
            multiplier = multiplier_list[0]*100 + multiplier_list[1]*10 + multiplier_list[2]
            product = mult*multiplier
            product_list = list(str(product))
            product_list.sort()
           
            for j in multiplier_list:
                t_pan2.remove(j)
            t_pan2.sort()
            a = t_pan2[0]*1000 + t_pan2[1]*100 + t_pan2[2]*10 + t_pan2[3]*1
            b = int(product_list[0])*1000 + int(product_list[1])*100 + int(product_list[2])*10 + int(product_list[3])
            if a == b and len(product_list) == 4:
                pan_product.append(product)
    return pan_product

#this takes about 10 seconds in trinket
def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)

p = set()
for i in range(2,  60):
    start = 1234 if i < 10 else 123 
    for j in range(start, 10000//i):
        if is_pandigital(str(i) + str(j) + str(i*j)): p.add(i*j)

print "Sum of products =", sum(p)
