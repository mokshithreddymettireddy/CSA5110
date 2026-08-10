# Q9 - Playfair Cipher Decryption
# Given ciphertext:
# KXJEY UREBE ZWEHE WRYTU HEYFS
# KREHE GOYFI WTTTU OLKSY CAJPO
# BOTEI ZONTX BYBNT GONEY CUZWR
# GDSON SXBOU YWRHE BAAHY USEDQ

# The question does not print the keyword/key square.
# The program therefore accepts a 5x5 Playfair matrix as input.
# I/J are normally combined in Playfair.

ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

print("Enter the 5 Playfair rows.")
print("Use I/J as one cell if your matrix combines I and J.")

matrix = []
for i in range(5):
    row = input(f"Row {i+1}: ").replace(" ", "").upper()
    if len(row) != 5:
        raise ValueError("Each row must contain exactly 5 letters.")
    matrix.append(row)

pos = {}
for r in range(5):
    for c in range(5):
        pos[matrix[r][c]] = (r, c)

def locate(ch):
    ch = ch.upper()
    if ch == "J" and "J" not in pos and "I" in pos:
        ch = "I"
    return pos[ch]

def decrypt_pair(a, b):
    ra, ca = locate(a)
    rb, cb = locate(b)

    if ra == rb:
        return matrix[ra][(ca - 1) % 5] + matrix[rb][(cb - 1) % 5]
    elif ca == cb:
        return matrix[(ra - 1) % 5][ca] + matrix[(rb - 1) % 5][cb]
    else:
        return matrix[ra][cb] + matrix[rb][ca]

clean = ''.join(ch for ch in ciphertext.upper() if ch.isalpha())

if len(clean) % 2:
    raise ValueError("Ciphertext must contain an even number of letters.")

plaintext = ""
for i in range(0, len(clean), 2):
    plaintext += decrypt_pair(clean[i], clean[i + 1])

print("\nCiphertext:")
print(clean)
print("\nDecrypted text:")
print(plaintext)
