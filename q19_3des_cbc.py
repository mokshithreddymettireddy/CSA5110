# Q19 - 3DES CBC Mode Encryption
# Uses Triple DES (3DES) in CBC mode.
# Requires PyCryptodome:
#     pip install pycryptodome
#
# Security: 3DES is stronger than single DES.
# Performance: 3DES is slower because it performs DES three times.
# For a real new system, AES is generally preferred over 3DES.

try:
    from Crypto.Cipher import DES3
except ImportError:
    print("Install dependency first: pip install pycryptodome")
    raise

from Crypto.Random import get_random_bytes

def pad(data, block=8):
    n = block - len(data) % block
    return data + bytes([n])*n

def encrypt_cbc(message, key=None, iv=None):
    if key is None:
        key = DES3.adjust_key_parity(get_random_bytes(24))
    if iv is None:
        iv = get_random_bytes(8)

    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message))
    return key, iv, ciphertext

message = input("Enter message: ").encode()

key, iv, ciphertext = encrypt_cbc(message)

print("\n3DES CBC encryption")
print("Key        :", key.hex().upper())
print("IV         :", iv.hex().upper())
print("Ciphertext :", ciphertext.hex().upper())

print("\nChoice:")
print("a. Security  -> 3DES is stronger than single DES.")
print("b. Performance -> single DES is faster than 3DES.")
print("For modern applications, AES is normally preferred over both.")
