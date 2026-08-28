# Question 40: Automated Frequency Attack on Monoalphabetic Substitution Cipher
# Produces possible plaintext candidates in rough order of likelihood.

from collections import Counter

STANDARD_FREQUENCY_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

COMMON_PATTERNS = [
    "THE", "AND", "ING", "ION", "TH", "HE",
    "IN", "ER", "AN", "RE", "ON", "AT"
]


def build_candidate(ciphertext, offset):
    letters = [c.upper() for c in ciphertext if c.isalpha()]
    counts = Counter(letters)

    ordered_cipher = [
        item[0] for item in counts.most_common()
    ]

    mapping = {}

    for i, cipher_letter in enumerate(ordered_cipher):
        mapping[cipher_letter] = STANDARD_FREQUENCY_ORDER[
            (i + offset) % 26
        ]

    result = ""

    for ch in ciphertext:
        if ch.isalpha():
            replacement = mapping.get(ch.upper(), ch.upper())
            result += replacement if ch.isupper() else replacement.lower()
        else:
            result += ch

    return result, mapping


def calculate_score(text):
    upper = text.upper()
    score = 0

    for pattern in COMMON_PATTERNS:
        score += upper.count(pattern) * len(pattern)

    return score


def main():
    ciphertext = input("Enter ciphertext: ")
    top_n = int(input("Give me the top how many possible plaintexts? "))

    candidates = []

    # Create multiple possible frequency mappings
    for offset in range(26):
        plaintext, mapping = build_candidate(ciphertext, offset)
        score = calculate_score(plaintext)

        candidates.append((score, plaintext, mapping))

    candidates.sort(reverse=True, key=lambda x: x[0])

    print("\nTop possible plaintext candidates:\n")

    for i, (score, plaintext, mapping) in enumerate(
        candidates[:top_n], start=1
    ):
        print(f"Candidate {i} - Likelihood Score: {score}")
        print("Plaintext:", plaintext)
        print("Mapping:", mapping)
        print()


if __name__ == "__main__":
    main()
