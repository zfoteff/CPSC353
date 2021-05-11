"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [3/28/2021]
   Author/Source: Paul DePalma
   Assignment: Project 10
   Description: Implementation of the Diffie-Hellman Cipher
"""
import random

"""
    pre: size is an exponent 2^size
    post: returns large prime, and a primitive root g mod p
"""
def param_gen(size):
    p = next_prime(random.randint(1, 2^size))
    g = primitive_root(p)
    return p, g


"""
    pre: p, and g are returned by param_gen
    post: returns public key A and a
"""
def alice(p, g):
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    return A, a


"""
    pre: p, g are returned by param_gen
    post: returns B and b
"""
def bob(p, g):
    b = random.randint(1, p-1)
    B = pow(g, b, p)
    return B, b


"""
    pre: p is returned by param_get, b is from Bob, A is from Alice
    post: returnes k_bob
"""
def bob_key(p, b, A):
    k_bob = power_mod(A, b, p)
    return k_bob


"""
    pre: p is returned by param_gen, a is from Alice, and B is from Bob
    post: returns k_alice
"""
def alice_key(p, a, B):
    k_alice = power_mod(B, a, p)
    return k_alice


"""
    Main
"""
def main():
    p, g = param_gen(45)
    A, a = alice(p, g)
    B, b = bob(p, g)
    a_key = alice_key(p, a, B)
    b_key = bob_key(p, b, A)

    print("Alice's key:\t\t"+a_key)
    print("Bob's key:\t\t"+b_key)
