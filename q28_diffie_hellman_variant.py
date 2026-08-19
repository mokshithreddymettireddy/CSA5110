# Q28 - Diffie-Hellman and the incorrect variant
#
# Correct DH:
#   Alice sends A = a^x mod q
#   Bob   sends B = a^y mod q
#   Shared key = a^(xy) mod q
#
# Proposed incorrect variant:
#   Alice sends x^a mod q
#   Bob   sends y^a mod q
#
# There is no straightforward common secret derived from these two values
# using the ordinary DH operation. In particular, (x^a)^y and (y^a)^x are
# both x^(ay) and y^(ax), which are generally different.
#
# A simple way to agree on a key is to use the standard Diffie-Hellman
# construction. Eve can observe public values but should not obtain the
# shared key under the discrete-logarithm assumption.
#
# This program demonstrates both the correct protocol and the failure of
# the x^a variant.

def correct_dh(q, a, x, y):
    A = pow(a, x, q)
    B = pow(a, y, q)
    alice_key = pow(B, x, q)
    bob_key = pow(A, y, q)
    return A, B, alice_key, bob_key

def wrong_variant(q, a, x, y):
    A = pow(x, a, q)
    B = pow(y, a, q)

    # Natural attempted analogue:
    alice_attempt = pow(B, x, q)
    bob_attempt = pow(A, y, q)

    return A, B, alice_attempt, bob_attempt

q = 23
a = 5
x = 6
y = 15

print("Q28: Diffie-Hellman demonstration")

A, B, k1, k2 = correct_dh(q, a, x, y)
print("\nCorrect Diffie-Hellman")
print("Alice public value:", A)
print("Bob public value  :", B)
print("Alice shared key  :", k1)
print("Bob shared key    :", k2)
print("Keys agree?       :", k1 == k2)

A2, B2, k3, k4 = wrong_variant(q, a, x, y)
print("\nIncorrect x^a mod q variant")
print("Alice public value:", A2)
print("Bob public value  :", B2)
print("Alice attempted key:", k3)
print("Bob attempted key  :", k4)
print("Keys agree?         :", k3 == k4)

print("\nSecurity notes:")
print("- In standard DH, Eve sees q, a, A and B but cannot efficiently")
print("  compute the shared key if the discrete logarithm problem is hard.")
print("- Eve also cannot efficiently recover x or y from a^x mod q.")
print("- The x^a variant is not a secure replacement for standard DH.")
print("- Use standard DH or a modern authenticated key-exchange protocol.")
