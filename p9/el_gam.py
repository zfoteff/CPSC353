"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [3/28/2021]
   Author/Source: Paul DePalma
   Assignment: Project 9
   Description: Implementation of the El Gamal Cipher
"""

import sys
import random

"""
Converts a string to a decimal digit sequence
msg_in is a string
"""
def txt_to_num(msg_in):
  #transforms string to the indices of each letter in the 8-bit ASCII table
  #ex: "AB" becomes [65,66]
  msg_idx = list(map(ord,msg_in))

  #The integers in the list, since they are ASCII, are in the range 0..255
  #These are treated, collectively, as a base 256 integer, but from left to right
  #rather than right to left
  #This sequence of integers is converted to base 10
  #ex: [65,66] = 65*256^0 + 66*256^1 = 16961
  num = ZZ(msg_idx,256)
  return num

"""
Converts a digit sequence to a string
num_in is a decimal integer, constructed from a string using txt_to_num
"""
def num_to_txt(num_in):
  #transforms the base 10 num_in to a list of base 256 digits. 256^0 is on the left
  msg_idx = num_in.digits(256)

  #maps each index to its associated character in the ascii table
  m = map(chr,msg_idx)

  #transforms the list to a string
  m = ''.join(m)
  return m



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



"""
    pre:    size is an exponent, 2^size
    post:   returns El Gamal parameters
            p: large prime
            a: primitive root
"""
def param_gen(size):
    prime_size = pow(2, size)
    p = next_prime(random.randint(prime_size, prime_size+100))
    a = mod(primitive_root(p),p)
    return p, a

"""
    pre:    p, a are the large prime and primitive root from param_gen, a mod p
    post:   returns public and private key
            A: private key
            B: public key
"""
def key_gen(p, a):
    A = random.randint(1, p-1)
    B = (a^A)
    print("A, B: (%i, %i)" %(A, B))
    return A, B

"""
    pre:    B, p, a are the components of a public digital signature, m is
            plaintext message to encrypt
    post:   returns digital signature ciphertext (c1, c2)
            c1 = a^k mod p
            c2 = Km mod p
"""
def encrypt(B, p, a, m):
    k = random.randint(1, p-1)
    new_m = Integer(txt_to_num(m))
    c1 = (a^k)
    c2 = []

    if new_m >= p:
        ## Decompose ciphertext
        print(input("m > p"))
        m_text = decompose(new_m)
        for each in m_text:
            c2.append((B^(k))*each)
    else:
        ##  Add cipher text to the array
        c2.append((B^(k))*new_m)

    print("C1, C2: (%i, %i)" %(c1, c2))
    return c1, c2

def decrypt (A, p, c1, c2):
    for each in c2:
        m = c2 / c1^A
        each = Integer(m % p)

    new_m = Integer(recompose(c2))
    new_m_text = num_to_txt(new_m)
    return new_m_text

"""
    -------- Main Function --------
"""
def main():
    message = input("Enter a string: ")
    size = Integer(input("Enter a size: "))
    p, a = param_gen(size)
    priv_key, pub_key = key_gen(p, a)
    c1, c2 = encrypt(pub_key, p, a, message)
    m = decrypt(priv_key, p, c1, c2)
    print("Decrypted message: "+m)


main()
