# Q20 - ECB vs CBC Error Propagation
#
# This is a simulation/explanation program.
# For CBC decryption:
#   P_i = D_K(C_i) XOR C_(i-1)
#
# If a bit error occurs in C1:
#   P1 becomes corrupted in many bits (because D_K(C1) changes)
#   P2 has the corresponding bit flipped because C1 is XORed directly
#   P3 and later blocks are unaffected.
#
# If a source bit in P1 changes before encryption:
#   C1 changes unpredictably
#   Therefore P1 and P2 are affected at the receiver,
#   but P3 onward are recovered correctly.
#
# ECB has no chaining, so an error in one ciphertext block affects only
# that block during decryption.

def explain():
    print("ECB:")
    print("  Error in ciphertext block C1 -> only P1 is affected.")
    print()
    print("CBC:")
    print("  Error in transmitted C1 -> P1 and P2 are affected.")
    print("  P3, P4, ... are NOT affected.")
    print()
    print("Q20(a): Are blocks beyond P2 affected?")
    print("  No. Blocks P3 onward are recovered correctly.")
    print()
    print("Q20(b): Bit error in source P1")
    print("  P1 error changes C1.")
    print("  At the receiver, P1 is corrupted unpredictably.")
    print("  P2 has the corresponding bit error.")
    print("  P3 onward are unaffected.")
    print()
    print("Summary:")
    print("  ECB: C_i error -> P_i only")
    print("  CBC: C_i error -> P_i plus one-bit effect in P_(i+1)")
    print("  Source P_i error -> C_i changes; receiver gets P_i corrupted,")
    print("  and the corresponding bit in P_(i+1) is flipped.")

if __name__ == "__main__":
    explain()
