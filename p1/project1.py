"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [XXXXX]
   Assignment: Project 1
   Description: Program implements the Transposition Cipher, a symmetric key
   cipher, as well as methods to encrypt and decrypt any given string
"""
import random

"""
Method returns a list containing all 26 ordered letters of the alphabet
"""
def a_list():
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #   Generates list of the letters of the alphabet
    a_list = [x for x in a]
    return a_list

"""
Generates a random permutation of the alphabet and returns that permutation to
be used as the key for the Transposition Cipher
"""
def key_gen():
    #   Create list of the letters of the alphabet
    perm = a_list()
    #   Shuffles that list in place
    random.shuffle(perm)
    return perm

"""
Returns the encryption of the plaintext string, p, using the random permutation
of the alphabet, key

p: Plaintext string to be encrypted
key: list with random permutation of the alphabet
"""
def encrypt(p, key):
    #   Empty ciphertext string
    c = ""

    #   Next sequence strips spaces, punctuation marks, and other characters
    #   not in the alphabet from the string and then makes the string uppercase
    #   for ease of handling later
    plaintext = p.replace(" ", "")
    plaintext = plaintext.strip(",.:;?!")
    plaintext = plaintext.upper()

    for x in plaintext:
        #   Retrieve the element from the key that corresponds with the ASCII #
        #   of each plain text character, then append that element to the
        #   ciphertext string for encryption
        c += key[ord(x)-65]

    return c

"""
Returns decryption of the ciphertext string, c, using the random permutation of
the alphabet, key
"""
def decrypt(c, key):
    #   Empty plaintext string
    p = ""
    #   Make an list containing key and all elements of the alphabet
    decypher = key + a_list()
    

    #   Sort first 26 elements into lexigraphical order, making the same swaps
    #   to the last 26 elements of the list
    for i in range(0, 25):
        #   If the ASCII value of the character is different than the index it
        #   exists at, swap it with the element at the correct index
        if (ord(i)-65 != i):
            temp = decypher[ord(i)-65]
            decypher[ord(i)-65] = decypher[i]
            decypher[i] = temp

            #   Make those same swaps to the alphabet section of list

    #   With k in lexographical order, parse each character in the ciphertext to
    #   construct the plaintext from the shuffled alphabet
    for x in c:
        p += decypher[ord(x+26)-65]

    return p

#   Main loop
while True:
    key = key_gen()
    userPlaintext = input("Enter a message to encode (No numbers) or 'q' to quit: ")
    if userPlaintext == "q":
        break

    userCiphertext = encrypt(userPlaintext, key)
    print("Your encrypted message is: "+userCiphertext)
    print("That message decrypted is: "+decrypt(userCiphertext, key)+"\n\n")
