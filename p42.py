text_file = open('p042_words.txt', 'r')
lines = text_file.read().split(',')
lines = map(lambda s: s[1:len(s)-1],lines)
lines.sort()

text_int_sum = [sum( [ ord(i) - 64 for i in x]) for x in lines]

count = 0
for j in text_int_sum:
    s1 = int(-.5 + (.25+2*j)**.5)
    if 2*j == s1*(s1 + 1):
        count +=1
