alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
cipherAlphabet = ("n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
key = dict(zip(alphabet, cipherAlphabet))
print(alphabet)
print(cipherAlphabet)

def ROT13 (message):

    ciphertext = []
    for l in plaintext:
        ciphertext.append(key[l])
    print(ciphertext)

    decryptedText = []
    for k in ciphertext:
        decryptedText.append(key[k])
    print(decryptedText)
