# Q16 - Automatic Letter Frequency Attack on a Monoalphabetic Cipher
# Uses simulated annealing / hill climbing with an English quadgram-like
# score. No manual substitution mapping is required.
#
# For best results, a longer ciphertext gives better statistical recovery.

import math
import random
import string
from collections import Counter

# Common English tetragrams/trigrams. The score is intentionally compact
# so the program is self-contained.
COMMON = {
    "TION": 4.0, "THER": 4.0, "WITH": 3.8, "HERE": 3.5,
    "OULD": 3.5, "IGHT": 3.5, "HAVE": 3.4, "THAT": 3.4,
    "ATIO": 3.3, "MENT": 3.3, "IONS": 3.2, "THIS": 3.2,
    "EVER": 3.0, "FROM": 3.0, "THE": 2.5, "AND": 2.3,
    "ING": 2.3, "ENT": 2.0, "HER": 2.0, "ERE": 1.8,
    "FOR": 1.8, "THA": 1.8, "NTH": 1.8, "WAS": 1.6,
    "ETH": 1.6, "VER": 1.6, "HIS": 1.6, "OFT": 1.5,
    "ST": 0.7, "ER": 0.7, "RE": 0.7, "AN": 0.7,
    "IN": 0.6, "ON": 0.6, "AT": 0.6, "EN": 0.6
}

COMMON_WORDS = {
    "THE": 15, "OF": 10, "AND": 10, "TO": 9, "IN": 9,
    "IS": 8, "YOU": 8, "THAT": 8, "IT": 7, "HE": 7,
    "WAS": 7, "FOR": 7, "ON": 6, "ARE": 6, "AS": 6,
    "WITH": 6, "HIS": 6, "THEY": 5, "I": 5, "AT": 5,
    "BE": 5, "THIS": 5, "HAVE": 5, "FROM": 5
}

ENGLISH_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decrypt(text, key):
    # key[cipher_index] = plaintext letter
    out = []
    for ch in text:
        if ch.isalpha():
            idx = ord(ch.upper()) - 65
            p = key[idx]
            out.append(p if ch.isupper() else p.lower())
        else:
            out.append(ch)
    return ''.join(out)

def score(text):
    u = text.upper()
    s = 0.0

    for gram, weight in COMMON.items():
        s += u.count(gram) * weight

    for word in u.split():
        w = ''.join(c for c in word if c.isalpha())
        s += COMMON_WORDS.get(w, 0)

    # Penalize unlikely single-letter words.
    words = u.split()
    for w in words:
        w = ''.join(c for c in w if c.isalpha())
        if len(w) == 1 and w not in ("A", "I"):
            s -= 8

    return s

def initial_key(ciphertext):
    freq = Counter(c for c in ciphertext.upper() if c.isalpha())
    cipher_order = ''.join(sorted(string.ascii_uppercase,
                                  key=lambda c: freq.get(c, 0),
                                  reverse=True))

    key = ['?'] * 26
    used = set()

    for c, p in zip(cipher_order, ENGLISH_ORDER):
        key[ord(c)-65] = p
        used.add(p)

    remaining = [c for c in string.ascii_uppercase if c not in used]
    j = 0
    for i in range(26):
        if key[i] == '?':
            key[i] = remaining[j]
            j += 1
    return key

def search(ciphertext, iterations=12000):
    key = initial_key(ciphertext)
    current = score(decrypt(ciphertext, key))
    best_key = key[:]
    best_score = current

    for i in range(iterations):
        a, b = random.sample(range(26), 2)
        key[a], key[b] = key[b], key[a]

        new_score = score(decrypt(ciphertext, key))
        temperature = max(0.1, 8.0 * (1 - i/iterations))

        if new_score > current or random.random() < math.exp(
                (new_score-current)/temperature):
            current = new_score
        else:
            key[a], key[b] = key[b], key[a]

        if current > best_score:
            best_score = current
            best_key = key[:]

    return best_score, decrypt(ciphertext, best_key), best_key

ciphertext = input("Enter monoalphabetic ciphertext: ")
n = int(input("How many plaintexts? [10]: ") or 10)
n = min(max(n, 1), 20)

candidates = []
for _ in range(n):
    candidates.append(search(ciphertext))

candidates.sort(reverse=True, key=lambda x: x[0])

print("\nPossible plaintexts:")
for i, (s, p, key) in enumerate(candidates, 1):
    print(f"\n{i}. Score = {s:.2f}")
    print(p)
