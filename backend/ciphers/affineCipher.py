alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
d2 = {v: k for k, v in alphabet.items()} #alphabet swapped

def encrypt(message, a, b):
    plaintext = message.casefold()
    for x in plaintext:
        eq = a * alphabet[x] + b
        result = eq % 26
        return("".join(d2[result]), end="")
