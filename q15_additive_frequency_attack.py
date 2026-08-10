# Q15 - Automatic Letter-Frequency Attack on an Additive Cipher
#
# An additive/Caesar cipher has only 26 possible shifts.
# This program tries all 26 shifts, scores each plaintext using
# English letter frequencies plus common English words/patterns,
# and prints the top N candidates.

from collections import Counter
import math

ENGLISH_FREQ = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97,
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.49,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10,
    'Z': 0.07
}

COMMON_WORDS = {
    "THE": 8, "AND": 7, "THAT": 6, "THIS": 6, "WITH": 5,
    "FROM": 5, "HAVE": 5, "FOR": 5, "NOT": 5, "ARE": 5,
    "YOU": 5, "WAS": 4, "BUT": 4, "ALL": 4, "CAN": 4,
    "ONE": 4, "BE": 4, "TO": 4, "OF": 4, "IN": 4,
    "IS": 4, "IT": 4, "AS": 3, "ON": 3, "AT": 3
}

COMMON_NGRAMS = {
    "TH": 2.0, "HE": 2.0, "IN": 1.5, "ER": 1.5, "AN": 1.5,
    "RE": 1.2, "ON": 1.2, "AT": 1.0, "EN": 1.0, "ND": 1.0,
    "THE": 3.0, "ING": 2.5, "AND": 2.5, "ION": 2.0
}

def decrypt(ciphertext, shift):
    result = []
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch)-base-shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def frequency_score(text):
    letters = [c for c in text.upper() if c.isalpha()]
    if not letters:
        return -float("inf")

    counts = Counter(letters)
    n = len(letters)

    # Chi-square score: lower is better, so return negative chi-square.
    chi = 0.0
    for letter, freq in ENGLISH_FREQ.items():
        expected = n * freq / 100
        observed = counts.get(letter, 0)
        if expected > 0:
            chi += (observed - expected) ** 2 / expected

    score = -chi

    # Reward common English words and n-grams.
    upper = text.upper()
    words = upper.split()

    for word in words:
        clean_word = ''.join(c for c in word if c.isalpha())
        if clean_word in COMMON_WORDS:
            score += COMMON_WORDS[clean_word]

    for gram, weight in COMMON_NGRAMS.items():
        score += upper.count(gram) * weight

    return score

def rank_candidates(ciphertext, top_n):
    candidates = []

    for shift in range(26):
        plain = decrypt(ciphertext, shift)
        score = frequency_score(plain)
        candidates.append((score, shift, plain))

    candidates.sort(reverse=True, key=lambda x: x[0])
    return candidates[:top_n]

ciphertext = input("Enter additive-cipher ciphertext: ")
n_text = input("How many possible plaintexts? [10]: ").strip()
top_n = int(n_text) if n_text else 10

top_n = max(1, min(top_n, 26))

results = rank_candidates(ciphertext, top_n)

print("\nPossible plaintexts, roughly ranked:")
print("-" * 70)

for rank, (score, shift, plaintext) in enumerate(results, 1):
    print(f"{rank:2}. Shift = {shift:2}, Score = {score:8.2f}")
    print(f"    {plaintext}")

print("\nNote: An additive cipher has only 26 shifts, so this program")
print("can exhaustively test every possible key without human intervention.")
