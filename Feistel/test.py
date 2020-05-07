# A test file for the Feistel network
import secrets
import random
import string

from Feistel import Feistel
import test_functions


s1 = ''.join([random.choice(string.ascii_letters) for i in range(0, 12)])
s2 = ''.join([random.choice(string.ascii_letters) for i in range(0, 13)])
s3 = ''

with open('test.txt', 'r') as datafile:
    s3 = datafile.read()

f = Feistel(test_functions.test_func1)

# create a set of random keys for encryption
keys= [secrets.randbits(16) for i in range(0, 13)]
rev_keys = keys.copy()
rev_keys.reverse()

encrypted1 = f.encrypt(s1, keys)
decrypted1 = f.encrypt(encrypted1, rev_keys)

encrypted2 = f.encrypt(s2, rev_keys)
decrypted2 = f.encrypt(encrypted2, keys)

encrypted3 = f.encrypt(s3, keys)
decrypted3 = f.encrypt(encrypted3, rev_keys)


print(s1, ':')
print('\t', encrypted1)
print('\t', decrypted1, '\n')

print(s2, ':')
print('\t', encrypted2)
print('\t', decrypted2, '\n')

print('contents of text.txt:')
print('\t', decrypted3, '\n')


