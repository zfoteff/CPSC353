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
    #   Make a copy of the key (k) in order to leave initial key unchanged
    k = key
    alpha_list = a_list()

    #   Implement selection sort to order k in lexographical order
    for i in range(0, len(k)-1):
        for j in range(i+1, len(k)):
            #   index of the lowest ASCII value character to be swapped with i
            min = i
            if (ord(k[j]) < ord(k[min])):
                #   If the ASCII value of the char at index i in the cipher text
                #   is lower than min, replace min with index of that char
                min = j

            #   Make necessary swaps to the key to get it in order
            temp = k[i]
            k[i] = k[min]
            k[min] = temp

            #   Make those same swaps to the alphabet list
            temp = alpha_list[i]
            alpha_list[i] = alpha_list[min]
            alpha_list[min] = temp

    #   With k in lexographical order, parse each character in the ciphertext to
    #   construct the plaintext from the shuffled alphabet
    for x in c:
        p += alpha_list[ord(x)-65]

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
