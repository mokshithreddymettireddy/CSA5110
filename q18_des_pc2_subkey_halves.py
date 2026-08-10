# Q18 - DES Subkey Structure
# DES starts with a 64-bit key. PC-1 removes the 8 parity bits,
# leaving 56 bits split into C and D, 28 bits each.
#
# PC-2 selects 48 bits from C||D:
#   first 24 selected bits come from the C half
#   second 24 selected bits come from the D half
# (with the standard PC-2 table, positions are arranged this way.)
#
# The program demonstrates this for every round.

PC1 = [
57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,
59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,
31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,
29,21,13,5,28,20,12,4
]

PC2 = [
14,17,11,24,1,5,3,28,15,6,21,10,
23,19,12,4,26,8,16,7,27,20,13,2,
41,52,31,37,47,55,30,40,51,45,33,48,
44,49,39,56,34,53,46,42,50,36,29,32
]

SHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

def bits(h, width):
    return [int(x) for x in f"{int(h,16):0{width}b}"]

def permute(b, t):
    return [b[i-1] for i in t]

def shift_left(b,n):
    return b[n:] + b[:n]

def hx(b):
    return f"{int(''.join(map(str,b)),2):0{len(b)//4}X}"

key = input("Enter DES key [133457799BBCDFF1]: ") or "133457799BBCDFF1"

b64 = bits(key,64)
b56 = permute(b64,PC1)
C,D = b56[:28],b56[28:]

print("After PC-1:")
print("C0 =", hx(C), " (28 bits)")
print("D0 =", hx(D), " (28 bits)")

for r,sh in enumerate(SHIFTS,1):
    C=shift_left(C,sh)
    D=shift_left(D,sh)
    selected=permute(C+D,PC2)

    first24=selected[:24]
    second24=selected[24:]

    print(f"\nRound {r}")
    print("C =", hx(C))
    print("D =", hx(D))
    print("First 24 bits :", hx(first24))
    print("Second 24 bits:", hx(second24))
    print("Subkey K{}    :".format(r), hx(selected))
