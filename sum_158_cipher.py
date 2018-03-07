# the is a substitution decryption that exchanged the characters between 32 and 126
# in a way that character 32 was put in the place of 126, 33 exchanged with 125,
# 34 with 124, etc. 
def decrypt(message):
    result = ""
    #loop over all letter in the message and subsitute it with its alternate
    for letter in message:
        result += chr(158 - ord(letter))

    return result

# main program begins here

# read the text file
with open('file_007271.txt', 'r') as f:
    encrypted_message = f.read()
    f.close()


decrypted_message = decrypt(encrypted_message)

print(decrypted_message)
