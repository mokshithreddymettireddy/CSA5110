# Q7 - Monoalphabetic/Substitution Cipher
# The ciphertext is the one supplied in the question.
# This program uses the standard frequency-analysis approach:
# 1. Count symbols
# 2. Start with likely E/T/H mappings
# 3. Apply a manually refined substitution table
#
# The symbol set contains non-ASCII characters, so Python strings are used.

from collections import Counter

ciphertext = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81
(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

print("Character frequency (most common first):")
for ch, count in Counter(ciphertext).most_common():
    if not ch.isspace():
        print(repr(ch), ":", count)

# A useful way to solve a substitution cipher is to build the mapping
# gradually from frequency, repeated patterns, and guessed words.
#
# Enter mappings as ciphertext_symbol=plaintext_letter.
# Example: 8=e
mapping = {}

print("\nEnter known mappings one at a time.")
print("Press Enter without typing anything when finished.")
while True:
    entry = input("Mapping (cipher=plain): ").strip()
    if not entry:
        break
    if "=" in entry:
        c, p = entry.split("=", 1)
        if len(c) == 1 and len(p) == 1:
            mapping[c] = p.lower()

def decode(text, mp):
    return ''.join(mp.get(ch, ch) for ch in text)

print("\nCurrent partial decryption:")
print(decode(ciphertext, mapping))
print("\nAdd more mappings and run the program again until the plaintext is recovered.")
