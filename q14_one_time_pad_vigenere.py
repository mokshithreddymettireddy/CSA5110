# Q14 - One-Time Pad Version of the Vigenere Cipher
# Encryption: C_i = (P_i + K_i) mod 26
# Decryption: P_i = (C_i - K_i) mod 26

def clean(text):
    return ''.join(c for c in text.upper() if c.isalpha())

def encrypt(plaintext, key):
    p = clean(plaintext)
    if len(p) != len(key):
        raise ValueError("Plaintext and key stream must have equal lengths.")

    result = ""
    for ch, k in zip(p, key):
        pval = ord(ch) - 65
        cval = (pval + k) % 26
        result += chr(cval + 65)
    return result

def decrypt(ciphertext, key):
    c = clean(ciphertext)
    if len(c) != len(key):
        raise ValueError("Ciphertext and key stream must have equal lengths.")

    result = ""
    for ch, k in zip(c, key):
        cval = ord(ch) - 65
        pval = (cval - k) % 26
        result += chr(pval + 65)
    return result

# Part (a)
plaintext = "send more money"
key1 = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt(plaintext, key1)

print("PART (a)")
print("Plaintext :", plaintext)
print("Key stream:", key1)
print("Ciphertext:", ciphertext)

print("\nCalculations:")
for ch, k, out in zip(clean(plaintext), key1, ciphertext):
    p = ord(ch) - 65
    c = ord(out) - 65
    print(f"{ch}({p}) + {k} = {c} -> {out}")

# Part (b)
target_plaintext = "cash not needed"
c = clean(ciphertext)
target = clean(target_plaintext)

key2 = []
for cipher_ch, plain_ch in zip(c, target):
    cv = ord(cipher_ch) - 65
    pv = ord(plain_ch) - 65
    key2.append((cv - pv) % 26)

print("\nPART (b)")
print("Ciphertext       :", ciphertext)
print("Desired plaintext:", target_plaintext)
print("Required key      :", key2)
print("Verification      :", decrypt(ciphertext, key2))

print("\nThis demonstrates the one-time-pad property:")
print("with a truly random key stream of the same length, a ciphertext")
print("can be made consistent with any plaintext of that length.")
