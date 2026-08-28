# Question 37: Letter Frequency Attack on Monoalphabetic Substitution Cipher
# Educational demonstration producing candidate plaintexts using frequency mapping.

from collections import Counter

ENGLISH_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def frequency_attack(ciphertext, top_n):
    letters = [c.upper() for c in ciphertext if c.isalpha()]
    freq = Counter(letters)

    # Sort ciphertext letters from most frequent to least frequent
    cipher_order = "".join(
        letter for letter, count in freq.most_common()
    )

    results = []

    # Generate shifted variations of frequency ranking
    for shift in range(26):
        mapping = {}

        for i, c in enumerate(cipher_order):
            mapping[c] = ENGLISH_ORDER[(i + shift) % 26]

        candidate = ""
        for ch in ciphertext:
            if ch.isalpha():
                plain = mapping.get(ch.upper(), ch.upper())
                candidate += plain if ch.isupper() else plain.lower()
            else:
                candidate += ch

        # Simple score based on common English words
        score = 0
        common_words = ["THE", "AND", "ING", "ION", "TH", "HE", "IN", "ER", "AN"]
        upper_candidate = candidate.upper()

        for word in common_words:
            score += upper_candidate.count(word)

        results.append((score, candidate))

    results.sort(reverse=True, key=lambda x: x[0])
    return results[:top_n]


def main():
    ciphertext = input("Enter ciphertext: ")
    top_n = int(input("How many possible plaintexts do you want? "))

    results = frequency_attack(ciphertext, top_n)

    print("\nTop possible plaintext candidates:\n")

    for i, (score, text) in enumerate(results, start=1):
        print(f"{i}. Score = {score}")
        print(text)
        print()


if __name__ == "__main__":
    main()
