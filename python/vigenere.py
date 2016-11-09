# Vigenere A-0 cipher (A=0, Z=25)
# s = string (plain or ciphertext), k = key, d = direction (1=encrypt, -1=decrypt)
def vigenere0(s,k,d=1):
    return ''.join([chr(97+(ord(p[0])-97+d*(ord(p[1])-97))%26) for p in zip(s,(k*len(s))[:len(s)])])

# ord('a') = 97
# chr(97) = 'A'

# plain = "hello"
# key = "yay"

# repeated_key = (key*(len(plain)))[:len(plain)]
# can't figure out how to use ceil (len(plain)/len(key)) without 'import math', which I want to avoid, so I exaggerate the length of the repeated_key to the worst case (a key of length 1).

# plain_key_zip = zip(plain, repeated_key)
