alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
rotatedAlphabet = ("n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
key = dict(zip(alphabet, rotatedAlphabet))
print(alphabet)
print(rotatedAlphabet)

def encrypt(message, key)
    try:
        ciphertext = []
        for l in message:
            ciphertext.append(key[l])
            print(cipherText)
    except:
        print("error. Please use only lowercase letters")

def decrypt(message, key)
    try:
        decryptedText = []
        for k in ciphertext:
            decryptedText.append(key[k])
        print(decryptedText)
    except:
        print("error. Please use only lowercase letters")
        
