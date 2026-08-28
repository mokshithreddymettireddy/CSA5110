# Question 35: One-Time Pad Version of Vigenere Cipher

import secrets


def generate_key(length):
    return [secrets.randbelow(26) for _ in range(length)]


def encrypt(plaintext, key):
    ciphertext = ""

    for i, char in enumerate(plaintext):
        if char.isupper():
            value = (ord(char) - ord("A") + key[i]) % 26
            ciphertext += chr(value + ord("A"))
        elif char.islower():
            value = (ord(char) - ord("a") + key[i]) % 26
            ciphertext += chr(value + ord("a"))
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""

    for i, char in enumerate(ciphertext):
        if char.isupper():
            value = (ord(char) - ord("A") - key[i]) % 26
            plaintext += chr(value + ord("A"))
        elif char.islower():
            value = (ord(char) - ord("a") - key[i]) % 26
            plaintext += chr(value + ord("a"))
        else:
            plaintext += char

    return plaintext


def main():
    plaintext = input("Enter plaintext: ")

    key = generate_key(len(plaintext))
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    print("\nOne-Time Pad Vigenere Cipher")
    print("Plaintext :", plaintext)
    print("Random Key:", key)
    print("Ciphertext:", ciphertext)
    print("Decrypted :", decrypted_text)


if __name__ == "__main__":
    main()
