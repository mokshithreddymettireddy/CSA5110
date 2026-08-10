# Q21 - Padding Motivation for ECB, CBC and CFB
# Padding: append a 1 bit followed by zero bits until the final block
# is complete. Even when the message is already block-aligned, a full
# padding block is added.
#
# Motivation:
# If padding were omitted for an already-aligned plaintext, the receiver
# could not reliably distinguish:
#   1. a message ending exactly at a block boundary, from
#   2. a message whose last data byte/bit happened to look like padding.
#
# Always padding gives the receiver an unambiguous rule for removing
# padding. It also prevents ambiguity between a real trailing 1/0 pattern
# and padding.

def pad_bits(bits, block_size):
    if not bits or any(c not in "01" for c in bits):
        raise ValueError("Enter a non-empty binary string.")

    # Always add a 1 bit, then enough 0 bits to reach the next block.
    padded = bits + "1"
    zeros = (-len(padded)) % block_size
    return padded + "0" * zeros

def unpad_bits(bits):
    if not bits or bits[-1] not in "01":
        raise ValueError("Invalid padded data.")

    i = len(bits)-1
    while i >= 0 and bits[i] == "0":
        i -= 1

    if i < 0 or bits[i] != "1":
        raise ValueError("Invalid padding.")

    return bits[:i]

block_size = int(input("Block/segment size in bits [8]: ") or 8)
data = input("Enter plaintext bits: ").strip()

padded = pad_bits(data, block_size)

print("\nOriginal :", data)
print("Padded   :", padded)
print("Blocks   :", [padded[i:i+block_size]
                   for i in range(0, len(padded), block_size)])

print("\nMotivation for padding an already-complete message:")
print("The receiver gets an unambiguous padding format.")
print("A complete plaintext still receives a new padding block,")
print("so the receiver can always remove padding using the same rule.")
