import itertools

def encrypt(message, input):
    plaintext = message.casefold()
    a = list(itertools.repeat([], input))
    try:
        for v in range(0, input):
            a[v].append(plaintext[v::input]) #the elements in list a are actually changing in tandem so I have to print only the last one
        ciphertext = "".join(a[len(a)-1])
        return(ciphertext) #return the last element of list a
    except:
        return("error. input must be an integer")
