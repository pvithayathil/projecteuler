import itertools, urllib2

file_url = 'https://projecteuler.net/project/resources/p059_cipher.txt'
cipher_text = map(int, urllib2.urlopen(file_url).read().split(','))

def decode(cipher_text, key_length, key_set, morsel):
    for key in itertools.product(key_set, repeat=key_length):
        msg =  [x^y for x, y in zip(cipher_text, itertools.cycle(key))]
        if morsel in ''.join(map(chr, msg)):
            return sum(msg)
    return "No solution"

print decode(cipher_text, 3, range(97, 123),' God ')
