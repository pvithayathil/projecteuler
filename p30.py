the_list = []

for i in range(2,1000000):
    check = 0
    a_number_list = list(str(i))
    for n in a_number_list:
        n = int(n)
        check += n**5
    if check == i:
        the_list.append(i)

sum(the_list)
        
