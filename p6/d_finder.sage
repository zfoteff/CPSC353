"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [3/21/2021]
   Assignment: Project 6
   Description: Program performs necessary calculations in order to  generate a public and private
   key for an RSA encryption system
"""

from sage.arith.misc import GCD
from sage.arith.misc import XGCD
import random

p1 = pow(2, 100)
p2 = pow(2, 150)
p = next_prime(random.randint(p1, p2))
q = next_prime(random.randint(p1, p2))
n = p * q
phi = (p-1)*(q-1)
e = 111
d = 1

while e < n:
    if ( GCD(e, phi) == 1 ):
        break
    
    e = e + 1

d = inverse_mod(e, phi)

print ("P: "+str(p))
print ("Q: "+str(q))
print ("N: "+str(n))
print ("E: "+str(e))
print ("D: "+str(d)+"\n")
print ("Public Key (n, e): (%i, %i)" %(n, e))
print ("Private Key (d): (%i)" %(d))
