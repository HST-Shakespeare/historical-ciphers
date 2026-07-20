import itertools
#creating the rails using itertools.repeat() function:
a = list(itertools.repeat([], 3))
#print(a)

input = 3
message = "guilford"
plaintext = tuple(message)
#using multiplication:
lst = [[]]*3
#print(lst)

def encrypt(rail, position):
    a[rail].append(message[position::3])
    print(a[rail])
encrypt(0, 0)
encrypt(1, 1)
encrypt(2, 2)