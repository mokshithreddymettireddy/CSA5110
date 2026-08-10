# Q11 - Playfair Cipher Keyspace
# Standard Playfair uses 25 letters (I/J combined).
# Number of possible 5x5 arrangements = 25!
# If row/column ordering is treated as part of the key, this is the raw keyspace.
# Approximate power of 2 is log2(25!).
#
# Effective unique keys:
# A Playfair square gives the same encryption transformation under:
#   - row/column permutations that preserve the rectangle relationships
#   - transposition of the square
#   - cyclic shifts of rows/columns
#
# A commonly used effective-key estimate is 25! / (2 * 25),
# accounting for 25 equivalent cyclic shifts and transposition.
# This program shows both estimates.

import math

raw_keys = math.factorial(25)
raw_log2 = math.log2(raw_keys)

effective_keys = raw_keys // 50
effective_log2 = math.log2(effective_keys)

print("Playfair raw keyspace = 25!")
print(f"25! = {raw_keys:,}")
print(f"Approximate power of 2: 2^{raw_log2:.2f}")

print("\nEffective keyspace estimate:")
print(f"25! / 50 = {effective_keys:,}")
print(f"Approximate power of 2: 2^{effective_log2:.2f}")

print("\nNote:")
print("This uses the standard equivalence estimate for Playfair squares.")
print("Different textbooks may use a slightly different convention for")
print("which equivalent transformations are factored out.")
