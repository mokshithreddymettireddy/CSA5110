# Q30 - CBC-MAC extension/forgery demonstration
#
# For a one-block message X:
#   T = CBC-MAC_K(X) = E_K(X)
#
# Let the two-block message be:
#   X || (X XOR T)
#
# Its CBC-MAC is:
#   E_K(E_K(X) XOR (X XOR T))
# = E_K(T XOR X XOR T)
# = E_K(X)
# = T
#
# Thus the adversary can construct a two-block message having the same
# CBC-MAC tag as X, without knowing K.

def xor_bytes(a, b):
    if len(a) != len(b):
        raise ValueError("Inputs must have the same length")
    return bytes(x ^ y for x, y in zip(a, b))

class ToyBlockCipher:
    """Tiny reversible cipher for demonstration only; NOT cryptographically secure."""
    def __init__(self, key):
        self.key = key

    def encrypt(self, block):
        # XOR with key is a toy permutation.
        return xor_bytes(block, self.key)

def cbc_mac_one_block(cipher, x):
    return cipher.encrypt(x)

def cbc_mac_two_blocks(cipher, x1, x2):
    t1 = cipher.encrypt(x1)
    return cipher.encrypt(xor_bytes(t1, x2))

key = bytes.fromhex("0f1e2d3c4b5a6978")
X = bytes.fromhex("1122334455667788")

cipher = ToyBlockCipher(key)

T = cbc_mac_one_block(cipher, X)
second_block = xor_bytes(X, T)

T_forged = cbc_mac_two_blocks(cipher, X, second_block)

print("Q30: CBC-MAC two-block forgery")
print("X                 =", X.hex())
print("MAC(X) = T        =", T.hex())
print("X XOR T           =", second_block.hex())
print("MAC(X || (X XOR T)) =", T_forged.hex())

print("\nSame tag?", T == T_forged)

print("\nConclusion:")
print("The adversary knows T = MAC(K, X).")
print("They construct X || (X XOR T).")
print("The resulting two-block message has the same CBC-MAC tag T.")
print("Therefore plain CBC-MAC is unsafe for variable-length messages.")
print("Use a construction designed for variable-length authentication,")
print("such as CMAC, rather than raw CBC-MAC.")
