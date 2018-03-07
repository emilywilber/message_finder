# looks for common words in the message
def has_keyword(message, keywords):
    message = " " + message

    for word in keywords:
        word = " " + word
        if word in message:
            return True

    return False        

# this is the same shift function from caesar
# modified to handle the case where the unicode value was way less than 32
def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        unicode_value += - 95
    elif unicode_value < 32:
        unicode_value += 95
        if unicode_value < 32:
            unicode_value += 95
    new_letter = chr(unicode_value)

    return new_letter



# This function uses a vigenere cipher to encrypt 'message' using the given 'keyword'.
# Note: the calculation used to set the shift amount here should match the one used in decrypt
# this is used for testing only
def vigenere_encrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        shift_amount = ord(keyword[ki])
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result

# This function uses a vigenere cipher to decrypt 'message'
# for the value e (in enigma) it shifts -101
def vigenere_decrypt(message, keyword):
    result = ""
    # keyword index goes 0, 1, 2, ... up to the number of letters in keyword 
    ki=0
    
    for letter in message:
        shift_amount = (-1) * ord(keyword[ki]) 
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result





# reads the given file and returns its contents
def readfile(filename):
    with open("file_012499.txt", 'r') as f:
        contents = f.read()
        f.close()
    return contents
    
### main program begins

# define a list of common words to look for
common = ["and" , "the", "message", "Message"]

   
keyword = "enigma"
encoded_file = "file_012499.txt"
extracted_message_path = "vigenere_decoded.txt"

encrypted_text = readfile(encoded_file)

decrypted_text = vigenere_decrypt(encrypted_text, keyword)
if has_keyword(decrypted_text, common)== True:
    print("***Found readable text in file:" + encoded_file)
    print("saving to "+extracted_message_path)
    with open(extracted_message_path, 'w') as f:
        f.write(decrypted_text)
else:
    print("***No readable text in file :" + encoded_file)
