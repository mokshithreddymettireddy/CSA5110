# Question 32: DSA Signature Demonstration

import hashlib
import random


def mod_inverse(a, m):
    return pow(a, -1, m)


def generate_dsa_signature(message, p, q, g, private_key):
    # A fresh random k is generated for every signature
    k = random.randint(1, q - 1)

    h = int(hashlib.sha256(message.encode()).hexdigest(), 16)
    r = pow(g, k, p) % q
    s = (mod_inverse(k, q) * (h + private_key * r)) % q

    return r, s, k


def main():
    # Small educational demonstration parameters
    p = 23
    q = 11
    g = 2
    private_key = 5

    message = input("Enter a message: ")

    r1, s1, k1 = generate_dsa_signature(message, p, q, g, private_key)
    r2, s2, k2 = generate_dsa_signature(message, p, q, g, private_key)

    print("\nFirst Signature")
    print("Random k =", k1)
    print("Signature =", (r1, s1))

    print("\nSecond Signature for the same message")
    print("Random k =", k2)
    print("Signature =", (r2, s2))

    print("\nExplanation:")
    if (r1, s1) != (r2, s2):
        print("Signatures are different because DSA uses a fresh random k for each signature.")
    else:
        print("The signatures happened to match in this small demonstration.")


if __name__ == "__main__":
    main()
