
def encrypt(message, key):
    result = ""
    # Loop through each character in the input message
    for char in message:
        # Check if the character is an alphabetic character
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")                
            result += chr((ord(char) - base + int(key)) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, key):
    result = ""
    # Loop through each character in the input message
    for char in message:
        # Check if the character is an alphabetic character
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            result += chr((ord(char) - base - int(key)) % 26 + base)
        # If the character is not alphabetic, add it to the result without changing it
        else:
            result += char
    return result