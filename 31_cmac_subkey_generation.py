# Question 31: CMAC Subkey Generation

def left_shift_one_bit(block, block_size):
    mask = (1 << block_size) - 1
    return (block << 1) & mask


def generate_subkeys(L, block_size):
    # Constants required for CMAC:
    # 64-bit block size  -> Rb = 0x1B
    # 128-bit block size -> Rb = 0x87
    if block_size == 64:
        Rb = 0x1B
    elif block_size == 128:
        Rb = 0x87
    else:
        raise ValueError("Only 64-bit and 128-bit block sizes are supported.")

    # Generate K1
    if (L >> (block_size - 1)) & 1:
        K1 = left_shift_one_bit(L, block_size) ^ Rb
    else:
        K1 = left_shift_one_bit(L, block_size)

    # Generate K2
    if (K1 >> (block_size - 1)) & 1:
        K2 = left_shift_one_bit(K1, block_size) ^ Rb
    else:
        K2 = left_shift_one_bit(K1, block_size)

    return K1, K2, Rb


def main():
    block_size = int(input("Enter block size (64 or 128): "))
    L_hex = input("Enter L in hexadecimal: ")
    L = int(L_hex, 16)

    K1, K2, Rb = generate_subkeys(L, block_size)
    hex_digits = block_size // 4

    print("\nCMAC Subkey Generation")
    print("Block size:", block_size, "bits")
    print("Rb constant:", format(Rb, "X"))
    print("K1 =", format(K1, f"0{hex_digits}X"))
    print("K2 =", format(K2, f"0{hex_digits}X"))


if __name__ == "__main__":
    main()
