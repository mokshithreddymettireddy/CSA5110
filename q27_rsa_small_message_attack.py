# Q27 - RSA encrypting each alphabetic character separately
# Attack: because the message space is only 26 values, an attacker can
# encrypt all 26 possible characters and build a lookup table.

def rsa_encrypt(m, e, n):
    return pow(m, e, n)

# Educational RSA parameters
p, q = 61, 53
n = p * q
e = 17

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Build codebook: ciphertext -> plaintext character
codebook = {}
for i, ch in enumerate(alphabet):
    codebook[rsa_encrypt(i, e, n)] = ch

message = "HELLO"
ciphertext = [rsa_encrypt(alphabet.index(ch), e, n) for ch in message]

print("Q27: Codebook attack on character-by-character RSA")
print("n =", n, "e =", e)
print("Plaintext :", message)
print("Ciphertext:", ciphertext)

recovered = "".join(codebook[c] for c in ciphertext)
print("Recovered :", recovered)

print("\nMost efficient attack:")
print("1. Compute RSA encryption of every possible value 0..25.")
print("2. Store ciphertext-to-character mappings.")
print("3. Replace every received ciphertext with its matching character.")

print("\nConclusion:")
print("This method is NOT secure. RSA is deterministic, and the plaintext")
print("domain contains only 26 possible values. Randomized padding such as")
print("RSA-OAEP should be used instead of encrypting each character directly.")
