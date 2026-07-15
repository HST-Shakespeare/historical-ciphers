import itertools
import random

message = "hellothere"  #the message that is to be sent
plaintext = tuple(message)
#print(plaintext)

boxLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#the letters inside the ADFGVX square
random.shuffle(boxLetters)
boxValues = ["AA", "AD", "AF", "AG", "AV", "AX", "DA", "DD", "DF", "DG", "DV", "DX", "FA", "FD", "FF", "FG", "FV", "FX",
             "GA", "GD", "GF", "GG", "GV", "GX", "VA", "VD", "VF", "VG", "VV", "VX", "XA", "XD", "XF", "XG", "XV", "XX"]
#the square's coordinates
boxKey = dict(zip(boxLetters, boxValues))
#print(boxKey)
diagraphList = []
for l in plaintext:
    diagraphList.append(boxKey[l])
#print(diagraphList)
substitutedText = list(itertools.chain.from_iterable(diagraphList))
#print(substitutedText)

z = []
o = []
e = []
def transpose(letter, start):
  letter.append(substitutedText[start::3])
transpose(z, 0)
transpose(o, 1)
transpose(e, 2)

encryptedMessage = tuple(itertools.chain.from_iterable(z+o+e))
print(encryptedMessage)
