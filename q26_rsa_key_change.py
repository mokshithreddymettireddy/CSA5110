# Q26 - RSA: Is changing e and d safe if the modulus n is reused?
# Answer: No. If Bob's private key d is leaked and he keeps the same n,
# the attacker may be able to factor n / recover the RSA private structure
# from the leaked key. Generating a new (e,d) pair with the same n does not
# provide the same security as generating a fresh modulus.

from math import gcd

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    return pow(c, d, n)

# Small educational example only
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

e_old = 17
d_old = mod_inverse(e_old, phi)

e_new = 7
d_new = mod_inverse(e_new, phi)

message = 42
cipher = rsa_encrypt(message, e_new, n)
plain = rsa_decrypt(cipher, d_new, n)

print("Q26: RSA key change with same modulus")
print("n =", n)
print("Old public/private pair: e =", e_old, ", d =", d_old)
print("New public/private pair: e =", e_new, ", d =", d_new)
print("Message:", message)
print("Ciphertext:", cipher)
print("Decrypted:", plain)

print("\nConclusion:")
print("NOT SAFE in general.")
print("Changing only e and d while reusing the leaked modulus n is not a")
print("proper recovery from a compromised RSA private key.")
print("A fresh RSA key pair with a NEW modulus should be generated.")
