import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars =list(chars)
key = chars.copy()

random.shuffle(key)

# print( f" chars :{chars}")
# print( f" keys :{key}")
 

# ENCRYPT
plain_text = input("eneter a message to encrypt ")
cipher_test = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_test += key[index]

print(f" original message : {plain_text}")
print(f" encrypt message : {cipher_test}")

# DECRYPT
cipher_text= input("eneter a message to decrypt ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f" encrypt message : {cipher_test}")
print(f" original message : {plain_text}")
