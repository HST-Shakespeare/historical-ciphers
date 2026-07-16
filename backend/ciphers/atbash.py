
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
cipherAlphabet = ("z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a")
key = dict(zip(alphabet, cipherAlphabet))
print(alphabet)
print(cipherAlphabet)

def encrypt(message, key)

ciphertext = []
for l in message:
    ciphertext.append(key[l])
print(ciphertext)

decryptedText = []
for l in message:
    decryptedText.append(key[l])
print(decryptedText)
