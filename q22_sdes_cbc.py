# Q22 - S-DES CBC Encryption and Decryption
# Implements Simplified DES (S-DES) with 8-bit blocks and 10-bit keys.
#
# Given test:
# IV = 10101010
# Plaintext = 00000001 00100011
# Key = 0111111101
# Expected ciphertext = 11110100 00001011

P10 = [3,5,2,7,4,10,1,9,8,6]
P8  = [6,3,7,4,8,5,10,9]
IP  = [2,6,3,1,4,8,5,7]
IP_INV = [4,1,3,5,7,2,8,6]
EP = [4,1,2,3,2,3,4,1]
P4 = [2,4,3,1]

S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a,b):
    return ''.join(str(int(x)^int(y)) for x,y in zip(a,b))

def generate_keys(key):
    p10 = permute(key, P10)
    left, right = p10[:5], p10[5:]

    left = left_shift(left,1)
    right = left_shift(right,1)
    k1 = permute(left+right, P8)

    left = left_shift(left,2)
    right = left_shift(right,2)
    k2 = permute(left+right, P8)

    return k1,k2

def sbox(bits, box):
    row = int(bits[0]+bits[3],2)
    col = int(bits[1]+bits[2],2)
    return f"{box[row][col]:02b}"

def fk(bits, key):
    left,right = bits[:4],bits[4:]
    expanded = permute(right,EP)
    mixed = xor(expanded,key)

    s = sbox(mixed[:4],S0) + sbox(mixed[4:],S1)
    p4 = permute(s,P4)

    return xor(left,p4)+right

def switch(bits):
    return bits[4:]+bits[:4]

def encrypt_block(plain,k1,k2):
    x = permute(plain,IP)
    x = fk(x,k1)
    x = switch(x)
    x = fk(x,k2)
    return permute(x,IP_INV)

def decrypt_block(cipher,k1,k2):
    x = permute(cipher,IP)
    x = fk(x,k2)
    x = switch(x)
    x = fk(x,k1)
    return permute(x,IP_INV)

def cbc_encrypt(plaintext, iv, k1, k2):
    result=[]
    previous=iv
    for i in range(0,len(plaintext),8):
        block=plaintext[i:i+8]
        x=xor(block,previous)
        c=encrypt_block(x,k1,k2)
        result.append(c)
        previous=c
    return ''.join(result)

def cbc_decrypt(ciphertext, iv, k1, k2):
    result=[]
    previous=iv
    for i in range(0,len(ciphertext),8):
        c=ciphertext[i:i+8]
        x=decrypt_block(c,k1,k2)
        p=xor(x,previous)
        result.append(p)
        previous=c
    return ''.join(result)

key=input("Key (10 bits) [0111111101]: ") or "0111111101"
iv=input("IV (8 bits) [10101010]: ") or "10101010"
plain=input("Plaintext (multiple of 8 bits) [0000000100100011]: ") or "0000000100100011"

k1,k2=generate_keys(key)

cipher=cbc_encrypt(plain,iv,k1,k2)
recovered=cbc_decrypt(cipher,iv,k1,k2)

print("\nK1:",k1)
print("K2:",k2)
print("Ciphertext:", ' '.join(cipher[i:i+8] for i in range(0,len(cipher),8)))
print("Recovered :", ' '.join(recovered[i:i+8] for i in range(0,len(recovered),8)))
print("\nExpected test ciphertext: 11110100 00001011")
