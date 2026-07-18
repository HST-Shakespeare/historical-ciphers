import random

alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
alphabet2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
random.shuffle(alphabet2)  #the cipher alphabet
return(alphabet)
return(alphabet2)  #the alphabets lined up
substitutionKey = dict(zip(alphabet, alphabet2))
decryptionKey = dict(zip(alphabet2, alphabet))

def encrypt(message):
    plaintext = message.casefold()
    try:       
        cipherText = []
        for l in plaintext:
            cipherText.append(substitutionKey[l])
        return(cipherText)
    except:
        return("Error. Please use only English letters")

def decrypt(ciphertext):
    try:
        decryptedText = []
        for k in cipherText:
            decryptedText.append(decryptionKey[k])
        return(decryptedText)
    except:
        return:("error. please use only English letters")
