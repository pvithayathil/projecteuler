text_file = open('p022_names.txt', 'r')
lines = text_file.read().split(',')
lines = map(lambda s: s[1:len(s)-1],lines)
lines.sort()



def sum_str(a_str):
    sum_val = 0
    for character in a_str:
        sum_val += ord(character) - 96

    return sum_val

lines = map(lambda s: sum_str(s.lower()), lines)    
total = 0
for i in range(0,len(lines)):
    total += (i+1)*lines[i]

print total
