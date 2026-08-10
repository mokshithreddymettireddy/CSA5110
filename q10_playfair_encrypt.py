# Q10 - Playfair Cipher Encryption
# Given Playfair matrix:
#
# M F H I/J K
# U N O P Q
# Z V W X Y
# E L A R G
# D S T B C
#
# Encrypt:
# "Must see you over Cadogan West. Coming at once"

matrix = [
    ["M", "F", "H", "I", "K"],
    ["U", "N", "O", "P", "Q"],
    ["Z", "V", "W", "X", "Y"],
    ["E", "L", "A", "R", "G"],
    ["D", "S", "T", "B", "C"]
]

pos = {}
for r in range(5):
    for c in range(5):
        pos[matrix[r][c]] = (r, c)

def prepare(text):
    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    text = text.replace("J", "I")

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            pairs.append(a + "X")
            i += 1
        else:
            b = text[i + 1]
            if a == b:
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
    return pairs

def encrypt_pair(a, b):
    ra, ca = pos[a]
    rb, cb = pos[b]

    if ra == rb:
        return matrix[ra][(ca + 1) % 5] + matrix[rb][(cb + 1) % 5]
    elif ca == cb:
        return matrix[(ra + 1) % 5][ca] + matrix[(rb + 1) % 5][cb]
    else:
        return matrix[ra][cb] + matrix[rb][ca]

message = "Must see you over Cadogan West. Coming at once"

pairs = prepare(message)
ciphertext = ''.join(encrypt_pair(a, b) for a, b in pairs)

print("Plaintext:", message)
print("Prepared pairs:", ' '.join(pairs))
print("Ciphertext:", ' '.join(ciphertext[i:i+5] for i in range(0, len(ciphertext), 5)))
