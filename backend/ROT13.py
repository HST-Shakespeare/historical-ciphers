alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
cipherAlphabet = ("n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m")
substitutionKey = dict(zip(alphabet, cipherAlphabet))
print(alphabet)
print(cipherAlphabet)

message = "rotcipher"  #generalize
plaintext = tuple(message)

ciphertext = []
for l in plaintext:
    ciphertext.append(substitutionKey[l])
print(ciphertext)

decryptedText = []
decryptionKey = dict(zip(cipherAlphabet, alphabet))
for k in ciphertext:
    decryptedText.append(decryptionKey[k])
print(decryptedText)