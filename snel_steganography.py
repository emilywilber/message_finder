import blue_steganography
## let's try to decode the message in jmann.png and save the output to stegan_output
encoded_image =  "jlmann.png"
blue_steganography.extract_message(encoded_image, "stegan_output.txt")


# DEBUGGING BELOW
#  That didn't work... let's encode a message from secret.txt with jlmann.png and
# save it to jlmann2.png
message_file = "secret.txt"
original_image = "jlmann.png"
encoded_image =  "jlmann2.png"
blue_steganography.hide_message(message_file, original_image, encoded_image)

# great let's now decode jlmann2.png and save the output to stegan_output2.txt
encoded_image =  "jlmann2.png"
blue_steganography.extract_message(encoded_image, "stegan_output2.txt")


