# Question 34: ECB, CBC and CFB Modes
# Install dependency first:
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def main():
    plaintext = input("Enter plaintext: ").encode()

    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    print("\nOriginal Plaintext:")
    print(plaintext.decode())

    # ECB MODE
    ecb_cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(plaintext, AES.block_size)
    ecb_ciphertext = ecb_cipher.encrypt(padded_data)

    print("\n--- ECB MODE ---")
    print("Ciphertext:", ecb_ciphertext.hex())

    ecb_decrypt = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(ecb_decrypt.decrypt(ecb_ciphertext), AES.block_size)
    print("Decrypted:", decrypted.decode())

    # CBC MODE
    cbc_cipher = AES.new(key, AES.MODE_CBC, iv)
    cbc_ciphertext = cbc_cipher.encrypt(padded_data)

    print("\n--- CBC MODE ---")
    print("IV:", iv.hex())
    print("Ciphertext:", cbc_ciphertext.hex())

    cbc_decrypt = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cbc_decrypt.decrypt(cbc_ciphertext), AES.block_size)
    print("Decrypted:", decrypted.decode())

    # CFB MODE
    cfb_cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    cfb_ciphertext = cfb_cipher.encrypt(plaintext)

    print("\n--- CFB MODE ---")
    print("IV:", iv.hex())
    print("Ciphertext:", cfb_ciphertext.hex())

    cfb_decrypt = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    decrypted = cfb_decrypt.decrypt(cfb_ciphertext)
    print("Decrypted:", decrypted.decode())


if __name__ == "__main__":
    main()
