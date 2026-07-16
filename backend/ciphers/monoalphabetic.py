import random

message = "joshuakcheng"
plaintext = tuple(message)
#print(plaintext)
alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
alphabet2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
random.shuffle(alphabet2)  #the cipher alphabet
print(alphabet)
print(alphabet2)  #the alphabets lined up
substitutionKey = dict(zip(alphabet, alphabet2))

cipherText = []
for l in plaintext:
    cipherText.append(substitutionKey[l])
print(cipherText)

decryptionKey = dict(zip(alphabet2, alphabet))
decryptedText = []
for k in cipherText:
    decryptedText.append(decryptionKey[k])
print(decryptedText)
