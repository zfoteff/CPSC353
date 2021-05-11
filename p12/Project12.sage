"""
   Name: Zac Foteff
   Class: CPSC 353
   Date Submitted: [5/5/2021]
   Assignment: Project 12
   Description: Implementation of MD2 Cipher
"""
import sys

#   Return a list containing all the digits of a number
def digit_list(n):
  d_list = []
  nums = str(n)
  for num in nums:
    if num == ".":
      continue

    d_list.append(num)

  return d_list

#   Message is increased to be a multiple of 16 bytes, i copies of the byte with
#   value
def padding (plaintext):
  p = list(map(ord, plaintext))

  counter = 0
  while len(p) % 16 != 0:
    p.append(p[counter])
    counter += 1
  return p


#   Append another 16 bytes to the padded message using the s-box permutation
def checksum (message, s_box):
  L = 0
  c = [0]*16
  for i in range(0, len(message)/16):
    for j in range(0, 16):
      c_val = message[16*i + j]
      c[j] = c[j]^^s_box[(c_val^^L)]
      L = c[j]

    new_m = message+c
    return new_m

#   Hash the checksum message using the s-box permutation
def hash (check_sum_msg, s_box):
  X = [0]*48
  for i in range(0, len(check_sum_msg)/16):
    for j in range(16):
      X[j+16] = check_sum_msg[16*i+j]
      X[j+32] = X[j+16] ^^ X[j]
    t = 0
    for j in range (18):
      for k in range(48):
        t = X[k] ^^ s_box[t]
        X[k] = t
      t = (t+j) % 256

  return X[0:15]

#   Generate an 256 element s-box using the digits of pi
def make_S():
  s_box = []
  num = ""
  pi_digits = digit_list(n(pi, digits=260))
  for i in range (0, len(pi_digits)-4):
    for j in range (0, 4):
      num = num+pi_digits[i+j]
    new_num = int(num) % 256
    s_box.append(new_num)
    num = ""
  return s_box

def md2 (message):
    padded_msg = padding(message);
    Sbox = make_S();
    checked_msg = checksum(padded_msg, Sbox)
    hash_msg = hash(checked_msg, Sbox)
    hash_txt = ""

    for each in hash_msg:
      num = (each%26) + 65
      each = chr(num)
      hash_txt += each

    print("Hash text: "+hash_txt)
