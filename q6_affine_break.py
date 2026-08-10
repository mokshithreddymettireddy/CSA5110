# Q6 - Break an Affine Cipher
# Given: most frequent ciphertext letter = B -> plaintext e
#        second most frequent ciphertext letter = U -> plaintext t
# Affine encryption: C = (aP + b) mod 26

import string
from math import gcd

ciphertext = input("Enter ciphertext: ").strip()

# B = 1, e = 4
# U = 20, t = 19
# 4a + b = 1 (mod 26)
# 19a + b = 20 (mod 26)
# => 15a = 19 (mod 26), giving a = 3, b = 15

a, b = 3, 15
a_inv = pow(a, -1, 26)

def decrypt(text):
    result = []
    for ch in text:
        if ch.isalpha():
            x = ord(ch.lower()) - ord('a')
            p = (a_inv * (x - b)) % 26
            plain = chr(p + ord('a'))
            result.append(plain.upper() if ch.isupper() else plain)
        else:
            result.append(ch)
    return ''.join(result)

print("\nAssumed mapping: B -> E, U -> T")
print(f"Affine key: a = {a}, b = {b}")
print(f"Inverse of a: {a_inv}")
print("\nDecrypted message:")
print(decrypt(ciphertext))
