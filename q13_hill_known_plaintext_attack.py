# Q13 - Hill Cipher Known-Plaintext / Chosen-Plaintext Attack
# For a 2x2 Hill cipher:
#     C = K * P (mod 26)
#
# If enough plaintext-ciphertext pairs are known, construct:
#     P = [[p1, p3],
#          [p2, p4]]
#     C = [[c1, c3],
#          [c2, c4]]
#
# Then:
#     K = C * P^-1 (mod 26)
#
# This program demonstrates recovering a 2x2 key from two
# plaintext digraphs and their corresponding ciphertext digraphs.

MOD = 26

def inv_mod(a, m):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    raise ValueError(f"{a} has no inverse modulo {m}.")

def matrix_inverse_2x2(M):
    a,b = M[0]
    c,d = M[1]
    det = (a*d - b*c) % MOD
    det_inv = inv_mod(det, MOD)
    return [
        [(det_inv*d) % MOD, (det_inv*(-b)) % MOD],
        [(det_inv*(-c)) % MOD, (det_inv*a) % MOD]
    ]

def multiply(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def text_to_nums(s):
    return [ord(c.upper())-65 for c in s if c.isalpha()]

def encrypt(text, K):
    nums = text_to_nums(text)
    if len(nums) % 2:
        nums.append(23)  # X
    out = ""
    for i in range(0, len(nums), 2):
        x,y = nums[i], nums[i+1]
        c1 = (K[0][0]*x + K[0][1]*y) % 26
        c2 = (K[1][0]*x + K[1][1]*y) % 26
        out += chr(c1+65) + chr(c2+65)
    return out

# Example secret key (unknown to the attacker)
secret_key = [
    [9,4],
    [5,7]
]

# Two known plaintext/ciphertext digraphs
known_plaintext = "MEET"
known_ciphertext = encrypt(known_plaintext, secret_key)

print("Known plaintext :", known_plaintext)
print("Known ciphertext:", known_ciphertext)

p = text_to_nums(known_plaintext)
c = text_to_nums(known_ciphertext)

P = [[p[0], p[2]],
     [p[1], p[3]]]

C = [[c[0], c[2]],
     [c[1], c[3]]]

print("\nP matrix:", P)
print("C matrix:", C)

P_inv = matrix_inverse_2x2(P)
print("P inverse:", P_inv)

recovered_key = multiply(C, P_inv)

print("\nRecovered Hill key:")
for row in recovered_key:
    print(row)

print("\nActual key:")
for row in secret_key:
    print(row)

print("\nVerification:")
test = "HELP"
print("Plaintext :", test)
print("Ciphertext:", encrypt(test, recovered_key))

print("\nA chosen-plaintext attack is even easier because the attacker")
print("can select convenient plaintext blocks that make P invertible.")
