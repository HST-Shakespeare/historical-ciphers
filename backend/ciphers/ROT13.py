alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
rotatedAlphabet = ("n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
key = dict(zip(alphabet, rotatedAlphabet))
return(alphabet)
return(rotatedAlphabet)

def encrypt(message, key)
    try:
        ciphertext = []
        for l in message:
            ciphertext.append(key[l])
            return(cipherText)
    except:
        return("error. Please use only lowercase letters")

def decrypt(message, key)
    try:
        decryptedText = []
        for k in ciphertext:
            decryptedText.append(key[k])
        return(decryptedText)
    except:
        return("error. Please use only lowercase letters")
        
