# set the key and alphabet to use
key      = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# encryption function
def encrypt(message):
    result = ""

    # loop over each letter in the input
    # find the location in the alphabet
    # add the corresponding letter from the key to the result
    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

#decryption function
def decrypt(message):
    result = ""

    # perform the encryption operatio in reverse
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result

# read a text file
with open('file_010005.txt', 'r') as f:
    encrypted_message = f.read()
    f.close()

# perform the decryption
decrypted_message = decrypt(encrypted_message)

print(decrypted_message)
