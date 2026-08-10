# Q23 - S-DES Counter (CTR) Mode
# S-DES: 8-bit block, 10-bit key.
#
# Counter starts at 00000000.
# Plaintext:
# 00000001 00000010 00000100
# Key:
# 0111111101
#
# Expected ciphertext:
# 00111000 01001111 00110010
#
# CTR encryption and decryption are identical:
# C_i = P_i XOR E_K(counter_i)
# P_i = C_i XOR E_K(counter_i)

P10=[3,5,2,7,4,10,1,9,8,6]
P8=[6,3,7,4,8,5,10,9]
IP=[2,6,3,1,4,8,5,7]
IP_INV=[4,1,3,5,7,2,8,6]
EP=[4,1,2,3,2,3,4,1]
P4=[2,4,3,1]

S0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

def permute(bits,t):
    return ''.join(bits[i-1] for i in t)

def ls(bits,n):
    return bits[n:]+bits[:n]

def xor(a,b):
    return ''.join(str(int(x)^int(y)) for x,y in zip(a,b))

def keys(key):
    p=permute(key,P10)
    l,r=p[:5],p[5:]
    l,r=ls(l,1),ls(r,1)
    k1=permute(l+r,P8)
    l,r=ls(l,2),ls(r,2)
    k2=permute(l+r,P8)
    return k1,k2

def sbox(x,box):
    row=int(x[0]+x[3],2)
    col=int(x[1]+x[2],2)
    return f"{box[row][col]:02b}"

def fk(x,k):
    l,r=x[:4],x[4:]
    e=permute(r,EP)
    z=xor(e,k)
    z=permute(sbox(z[:4],S0)+sbox(z[4:],S1),P4)
    return xor(l,z)+r

def enc(block,k1,k2):
    x=permute(block,IP)
    x=fk(x,k1)
    x=x[4:]+x[:4]
    x=fk(x,k2)
    return permute(x,IP_INV)

def ctr_process(data,key,start=0):
    k1,k2=keys(key)
    out=""
    for i in range(0,len(data),8):
        block=data[i:i+8]
        counter=f"{start+i//8:08b}"
        stream=enc(counter,k1,k2)
        out += xor(block,stream)
    return out

key=input("Key (10 bits) [0111111101]: ") or "0111111101"
plain=input("Plaintext [000000010000001000000100]: ") or "000000010000001000000100"

cipher=ctr_process(plain,key)
recovered=ctr_process(cipher,key)

print("Ciphertext:",' '.join(cipher[i:i+8] for i in range(0,len(cipher),8)))
print("Recovered :", ' '.join(recovered[i:i+8] for i in range(0,len(recovered),8)))
print("Expected  : 00111000 01001111 00110010")
