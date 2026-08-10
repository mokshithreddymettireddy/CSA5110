# Q12 - Hill Cipher Encryption and Decryption
# Key matrix:
# [9 4]
# [5 7]
#
# Encryption: C = K * P (mod 26)
# A=0, B=1, ..., Z=25

import math

K = [[9, 4],
     [5, 7]]

plaintext = "meet me at the usual place at ten rather than eight oclock"

def clean(text):
    return ''.join(c for c in text.upper() if c.isalpha())

def pairs(text):
    if len(text) % 2:
        text += "X"
    return [text[i:i+2] for i in range(0, len(text), 2)]

def encrypt_pair(pair):
    x1 = ord(pair[0]) - 65
    x2 = ord(pair[1]) - 65

    c1 = (9*x1 + 4*x2) % 26
    c2 = (5*x1 + 7*x2) % 26

    return chr(c1+65) + chr(c2+65), (x1, x2), (c1, c2)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    raise ValueError("No modular inverse.")

# Determinant = 9*7 - 4*5 = 43 = 17 mod 26
det = K[0][0]*K[1][1] - K[0][1]*K[1][0]
det_mod = det % 26
det_inv = mod_inverse(det_mod, 26)

# K^-1 = det^-1 * [[7,-4],[-5,9]] mod 26
K_inv = [
    [(det_inv*7) % 26, (det_inv*(-4)) % 26],
    [(det_inv*(-5)) % 26, (det_inv*9) % 26]
]

p = clean(plaintext)
print("Plaintext:", plaintext)
print("Cleaned plaintext:", p)
print("\nKey matrix:")
print(K)

print("\nEncryption calculations:")
ciphertext = ""
for pair in pairs(p):
    c, nums, out = encrypt_pair(pair)
    ciphertext += c
    print(f"{pair}: P=({nums[0]},{nums[1]}) -> "
          f"C=({out[0]},{out[1]}) -> {c}")

print("\nCiphertext:", ciphertext)

print("\nDeterminant:", det)
print("det mod 26:", det_mod)
print("det inverse mod 26:", det_inv)
print("Inverse key matrix:")
print(K_inv)

def decrypt_pair(pair):
    c1 = ord(pair[0]) - 65
    c2 = ord(pair[1]) - 65

    p1 = (K_inv[0][0]*c1 + K_inv[0][1]*c2) % 26
    p2 = (K_inv[1][0]*c1 + K_inv[1][1]*c2) % 26

    return chr(p1+65) + chr(p2+65), (c1,c2), (p1,p2)

print("\nDecryption calculations:")
recovered = ""
for pair in pairs(ciphertext):
    plain_pair, nums, out = decrypt_pair(pair)
    recovered += plain_pair
    print(f"{pair}: C=({nums[0]},{nums[1]}) -> "
          f"P=({out[0]},{out[1]}) -> {plain_pair}")

print("\nRecovered plaintext:", recovered)
