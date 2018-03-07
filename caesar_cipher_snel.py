# these first four functions are all unchanged from the original caesar 
def has_keyword(message, keywords):
    message = " " + message

    for word in keywords:
        word = " " + word
        if word in message:
            return True

    return False        

def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        unicode_value += - 95
    elif unicode_value < 32:
        unicode_value += 95

    new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    result = ""
    return encrypt(message, (-1) * shift_amount)

# list of common words to look for
common = ["and" , "the", "message"]

# read the text file
with open('file_001597.txt', 'r') as f:
    encrypted_message = f.read()
    f.close()

# loop through the range of shift values until one works and
# you can find a common word in the results
# then print the decrypted message and the shift value
for i in range(95):
    decrypted_message = decrypt(encrypted_message, i)
    if has_keyword(decrypted_message, common)== True:
        print(decrypted_message)
        print("shift value = %d" % i)


