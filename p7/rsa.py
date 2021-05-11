"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [3/28/2021]
   Author/Source: Paul DePalma
   Assignment: Project 6
   Description: Converts a string to a decimal digit sequence, encrypts that
   string using the RSA encryption algorithm and decrypts the message using the
   generated keys
"""

from sage.arith.misc import GCD
from sage.arith.misc import XGCD
import random

#   Pre: size is an exponent, as in 2^size.
#   Post: program returns the RSA public key,(n,e)  and the private key, d.
#   Comments: e is prime and of the form 2^r + 1, where r is an integer.  It does
#       not have to be large. 17 is a reasonable choice
def key_gen(size):
    #   Large primes p1, p2
    p1 = pow(2, size)
    p2 = pow(2, size+3)

    #   Generate two large primes greater than the inputed size
    p = next_prime(random.randint(p1, p2))
    q = next_prime(random.randint(p1, p2))

    #   Modulus n = p * q
    n = p*q
    phi = (p-1)*(q-1)
    e = 2
    counter = 0

    #   While e < n, look for a decent e value
    while e < n:
        if ( GCD(e, phi) == 1):
            if (counter == 5):
                break
            counter += 1

        e += 1

    d = inverse_mod(e, phi)

    #   Output the values to stream for the assignment
    print("p: \t\t"+str(p))
    print("q: \t\t"+str(q))
    print("n: \t\t"+str(n))
    print("phi: \t"+str(phi))
    print("e: \t\t"+str(e))
    print("d: \t\t"+str(d))

    #   Output the keys to the stream (testing)
    print ("pub key (n, e): (%i, %i)" %(n, e))
    print ("priv key (d): \t(%i)" %(d))

    return (n,e), (d)

#   Pre:  m_text is integer string representation of plain text to decompose
#   Post: returns array of integers <= 3 digits that comprise m_text
def decompose(m_text):
    dec_ints = []
    m = str(m_text)
    new_num = str("")

    for i in range(len(m)):
        new_num += m[i]

        # Add sets of three integers to the array
        if (i % 3 == 2 and i != 0):
            dec_ints.append(int(new_num))
            new_num = ""

    # If the end of the loop is reached and numbers still remain in new_num,
    # append them to list
    if (new_num != ""):
        dec_ints.append(int(new_num))

    return dec_ints


#    Pre: m_text is an integer string representation of plain text to recompose
#         by adding leading zeros back to ints that are shorter than 3 digits
#         except for the last value
#    Post: returns an integer string of the array
def recompose(m_text):
    new_m_text = []

    for i in range(0, len(m_text)-1):
        new_digits = str(m_text[i])

        if len(new_digits) == 2:
            new_m_text.append("0"+new_digits)

        elif len(new_digits) == 1:
            new_m_text.append("00"+new_digits)

        else:
            new_m_text.append(new_digits)

    # Add final element back into the new message
    new_m_text.append(str(m_text[-1]))
    return "".join(new_m_text)

#   Pre:  blocks is an array of integers
#   Post: an single integer is returned that is a combination of all the ints in
#         blocks
def combine_array(blocks):
    new_digits = int("".join(map(str, blocks)))
    return new_digits

#   Pre:  plain_text is a text string, chosen by the user
#         e, n are returned by key_gen
#   Post: returns the encryption of plain_text, using the RSA encryption
#         algorithm.
def encrypt(plain_text, n, e):
    #   enc(m,n,e) = m^e mod n
    blocks = decompose(txt_to_num(plain_text))

    # Encrypt each block
    for i in range(0, len(blocks)):
        c = power_mod(int(blocks[i]), e, n)
        blocks[i] = c

    return blocks

#   Pre: d, n are returned by key_gen.
#        c is ciphertext returned by encrypt.
#   Post: returns the decryption of the cipher_text, using the RSA algorithm
def decrypt(c, d, n):
    # dec(c,d,n) = c^d mod n
    message_ints = []
    for i in range (0, len(c)):
        m = power_mod(int(c[i]), d, n)
        message_ints.append(str(m))

    ## Fix issues with the removal of leading zeros
    message_ints = recompose(message_ints)
    message_ints = Integer(message_ints)
    message_ints = num_to_txt(message_ints)
    return message_ints


# Converts a string to a digit sequence
# msg_in is a string that is transformed into a sequence of integers
#   Source: Paul DePalma
def txt_to_num(msg_in):
    msg_idx = list(map(ord,msg_in))

    # The integers in the list, since they are ASCII, are in the range 0..255
    # These are treated, collectively, as a base 256 integer, but from left to right
    # rather than right to left
    # This sequence of integers is converted to base 10
    # ex: [65,66] = 65*256^0 + 66*256^1 = 16961
    num = ZZ(msg_idx,256)
    return num

# Converts a digit sequence to a string
# num_in is a decimal integer, constructed from a string using txt_to_num
def num_to_txt(num_in):
    # transforms the base 10 num_in to a list of base 256 digits. 256^0 is on the left
    msg_idx = num_in.digits(256)

    # maps each index to its associated character in the ascii table
    m = map(chr,msg_idx)

    # transforms the list to a string
    m = ''.join(m)
    return m

# Main function
def main():
    plain = input("Enter message to encrypt: ")
    prime_size = int(input("Enter size: "))

    # Input checking
    while prime_size < 2 or prime_size > 10000:
      prime_size = int(input("Please pick a number within the range [2,10000]: "))

    pub, priv = key_gen(prime_size)
    cipher = encrypt(plain, pub[0], pub[1])
    message = decrypt(cipher, priv, pub[0])
    print ("Plaintext:\t"+message)

#   Call main function
main()
