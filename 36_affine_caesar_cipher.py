# Question 36: Affine Caesar Cipher
# C = (a*p + b) mod 26

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            p = ord(ch.upper()) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + base)
        else:
            result += ch
    return result


def decrypt(text, a, b):
    a_inv = mod_inverse(a, 26)
    result = ""

    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            c = ord(ch.upper()) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + base)
        else:
            result += ch
    return result


def main():
    text = input("Enter plaintext: ")
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    # For one-to-one encryption, gcd(a,26) must be 1
    if gcd(a, 26) != 1:
        print("Invalid value of a.")
        print("For one-to-one mapping, gcd(a, 26) must be 1.")
        print("Valid values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25")
        return

    ciphertext = encrypt(text, a, b)
    plaintext = decrypt(ciphertext, a, b)

    print("\nCiphertext:", ciphertext)
    print("Decrypted text:", plaintext)


if __name__ == "__main__":
    main()
