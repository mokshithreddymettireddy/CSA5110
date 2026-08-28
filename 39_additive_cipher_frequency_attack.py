# Question 39: Letter Frequency Attack on Additive Cipher
# Tries all 26 possible Caesar/additive keys and ranks candidates.

ENGLISH_FREQUENCY = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70,
    'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
    'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
    'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
    'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
    'Z': 0.07
}


def decrypt(ciphertext, key):
    result = ""

    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            value = (ord(ch.upper()) - ord('A') - key) % 26
            result += chr(value + base)
        else:
            result += ch

    return result


def score_text(text):
    score = 0
    upper = text.upper()

    common_patterns = [
        "THE", "AND", "ING", "TION", "TH", "HE",
        "IN", "ER", "AN", "RE"
    ]

    for pattern in common_patterns:
        score += upper.count(pattern) * len(pattern)

    return score


def attack(ciphertext, top_n):
    candidates = []

    # Try every possible additive key
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = score_text(plaintext)

        candidates.append((score, key, plaintext))

    candidates.sort(reverse=True, key=lambda x: x[0])

    return candidates[:top_n]


def main():
    ciphertext = input("Enter ciphertext: ")
    top_n = int(input("Enter number of top candidates: "))

    results = attack(ciphertext, top_n)

    print("\nTop possible plaintexts:\n")

    for i, (score, key, plaintext) in enumerate(results, start=1):
        print(f"{i}. Key = {key}, Score = {score}")
        print("Plaintext:", plaintext)
        print()


if __name__ == "__main__":
    main()
