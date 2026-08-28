# Question 33: DES Encryption and Decryption
# Install dependency first:
# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def main():
    plaintext = input("Enter plaintext: ")
    key = input("Enter an 8-character DES key: ").encode()

    if len(key) != 8:
        print("Error: DES key must be exactly 8 bytes.")
        return

    cipher = DES.new(key, DES.MODE_ECB)

    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)

    print("\nEncryption")
    print("Plaintext:", plaintext)
    print("Ciphertext (Hex):", ciphertext.hex())

    decipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = decipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_data, DES.block_size).decode()

    print("\nDecryption")
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()
