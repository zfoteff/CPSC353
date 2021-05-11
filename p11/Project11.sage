"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [4/20/2021]
   Assignment: Project 11
   Description: Implementation of sDES for project 11 comparision assignment
"""

from sage.crypto.util import bin_to_ascii
from sage.crypto.block_cipher.sdes import SimplifiedDES
import random

def keygen():
    sdes = SimplifiedDES()
    k = sdes.list_to_string(sdes.random_key())
    return k

def encrypt(plaintext, key):
    sdes = SimplifiedDES()
    bin = BinaryStrings()
    p = bin.encoding(plaintext)
    print("Plaintext binary representation:\t"+str(p))
    c = sdes(p, key, algorithm="encrypt")

    cipher = bin_to_ascii(c)
    print("Encrypted text:\t"+str(c))
    return c

def decrypt(ciphertext, key):
    sdes = SimplifiedDES()
    p = sdes(ciphertext, key, algorithm="decrypt")

    plain = bin_to_ascii(p)
    print("Decrypted text:\t"+str(p))
    print("Decrypted plaintext:\t"+plain)

#   Main function
def main():
    p = input("Enter message to encrypt: ")
    k = keygen()
    c = encrypt(p, k)
    new_p = decrypt(c, k)

main()
