# Q17 - DES Decryption Key-Generation Scheme
# DES decryption uses the same round function as encryption,
# but the 16 subkeys are applied in reverse order:
# K16, K15, ..., K1.
#
# This program generates the 16 DES round keys and prints them
# in encryption order and decryption order.
#
# Key input: 64-bit hexadecimal DES key.
# Example: 133457799BBCDFF1

PC1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,
59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,
31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,28,20,12,4
]

PC2 = [
14,17,11,24,1,5,3,28,15,6,21,10,
23,19,12,4,26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,51,45,33,48,
44,49,39,56,34,53,46,42,50,36,29,32
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def hex_to_bits(h, width=64):
    return [int(b) for b in f"{int(h,16):0{width}b}"]

def permute(bits, table):
    return [bits[i-1] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def bits_to_hex(bits):
    value = int(''.join(map(str,bits)), 2)
    return f"{value:0{len(bits)//4}X}"

def generate_keys(hex_key):
    key_bits = hex_to_bits(hex_key, 64)
    pc1 = permute(key_bits, PC1)

    C = pc1[:28]
    D = pc1[28:]
    keys = []

    for shift in SHIFTS:
        C = left_shift(C, shift)
        D = left_shift(D, shift)
        subkey = permute(C+D, PC2)
        keys.append(subkey)

    return keys

key = input("Enter 64-bit DES key in hexadecimal [133457799BBCDFF1]: ")
if not key:
    key = "133457799BBCDFF1"

keys = generate_keys(key)

print("\nEncryption subkeys:")
for i, k in enumerate(keys, 1):
    print(f"K{i:2}: {bits_to_hex(k)}")

print("\nDecryption subkeys (reverse order):")
for i, k in enumerate(reversed(keys), 1):
    print(f"D{i:2} = K{17-i:2}: {bits_to_hex(k)}")

print("\nShift schedule:")
print(SHIFTS)
