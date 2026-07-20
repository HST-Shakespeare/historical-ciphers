import itertools
a = list(itertools.repeat([], 3))

message = "guilford"
plaintext = message.casefold()

def encrypt(input):
    try:
        for v in range(0, input)
            a[v].append(message[v::input])
        return(a[input-1])
    except:
        return("error. input must be an integer")
