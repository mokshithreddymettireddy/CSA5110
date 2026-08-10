# Q25 - RSA: Plaintext Block Sharing a Factor with n
# If a plaintext block m has a nontrivial common factor with n=pq,
# then gcd(m,n) reveals a factor of n.
#
# Therefore, even without the RSA private key, knowing that a plaintext
# block shares a factor with n can help factor n and recover the private key.
#
# If gcd(m,n)=g where 1 < g < n:
#     p = g
#     q = n/g
# Then compute phi(n) and d = e^(-1) mod phi(n).

import math

n=int(input("Enter RSA modulus n: "))
e=int(input("Enter public exponent e: "))
m=int(input("Enter the known plaintext block m: "))

g=math.gcd(m,n)

print("\ngcd(m,n) =",g)

if g==1:
    print("No nontrivial common factor was found.")
    print("This information does not factor n.")
elif g==n:
    print("m is a multiple of n; this does not reveal a nontrivial factor.")
else:
    p=g
    q=n//g
    phi=(p-1)*(q-1)

    try:
        d=pow(e,-1,phi)
    except ValueError:
        d=None

    print("A nontrivial factor has been discovered!")
    print("p =",p)
    print("q =",q)
    print("phi(n) =",phi)

    if d is not None:
        print("Private exponent d =",d)
        print("Private key =", (d,n))
    else:
        print("e has no inverse modulo phi(n).")
