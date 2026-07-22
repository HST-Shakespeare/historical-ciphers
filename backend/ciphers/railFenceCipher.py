import itertools

def encrypt(message, input):
    plaintext = message.casefold()
    a = list(itertools.repeat([], input))
    try:
        for v in range(0, input):
            a[v].append(plaintext[v::input]) #the elements in list a are actually changing in tandem
        ciphertext = "".join(a[len(a)-1])
        return(ciphertext) #return the last element of list a
    except:
        return("error. input must be an integer")

def decrypt(message, input)
    plaintext = message.casefold()
    b = list(itertools.repeat([], input))
    try:
        for w in range(0, input)
            b[w].append(plaintext[w::input])
        ciphertext = "".join(b[len(b-1)])
        return(ciphertext)
    except:
        return("error. please use only letters")
