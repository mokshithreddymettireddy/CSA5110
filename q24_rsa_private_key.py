# Q24 - RSA Private Key
# Given public key:
# e = 31
# n = 3599
#
# Find p and q by trial division, then compute:
# phi(n) = (p-1)(q-1)
# d = e^(-1) mod phi(n)

import math

e=31
n=3599

p=q=None
for candidate in range(2,int(math.sqrt(n))+1):
    if n % candidate == 0:
        p=candidate
        q=n//candidate
        break

if p is None:
    raise ValueError("Could not factor n.")

phi=(p-1)*(q-1)
d=pow(e,-1,phi)

print("Public key : (e,n) =", (e,n))
print("p =",p)
print("q =",q)
print("phi(n) =",phi)
print("d =",d)
print("Private key = (d,n) =", (d,n))

print("\nCheck:")
print("(e*d) mod phi(n) =", (e*d)%phi)
