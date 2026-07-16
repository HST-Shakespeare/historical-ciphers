
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
cipherAlphabet = ("z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a")
substitutionKey = dict(zip(alphabet, cipherAlphabet))
print(alphabet)
print(cipherAlphabet)

message = "atbashcipher"  #generalize
plaintext = tuple(message)

ciphertext = []
for l in plaintext:
    ciphertext.append(substitutionKey[l])
print(ciphertext)

decryptionKey = dict(zip(cipherAlphabet, alphabet))
decryptedText = []
for k in ciphertext:
    decryptedText.append(decryptionKey[k])
print(decryptedText)
