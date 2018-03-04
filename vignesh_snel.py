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

# This is the old caesar encryption.  Included here only for reference.
def encrypt(message, shift_amount):
    result = ""
    for letter in message:
        result += shift(letter, shift_amount)

    return result

# This function uses a vigenere cipher to encrypt 'message' using the given 'keyword'.
# Note: the calculation used to set the shift amount  here should match the one used in decrypt
def v_encrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        #shift_amount = ord(keyword[ki])-32-65
        shift_amount = ord(keyword[ki])-32
        #print ("encrypt shift amount = %d" % shift_amount)
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result

# This is the old caesar decryption.  Included here only for reference.
def decrypt(message, shift_amount):
    result = ""
    return encrypt(message, (-1) * shift_amount)

# This function uses a vigenere cipher to decrypt.
# it produces the same result as https://cryptii.com/vigenere-cipher
# for the value e (in enigma) it shifts -69
def e69_v_decrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        shift_amount = (-1) * ord(keyword[ki])+32 
        #print ("decrypt shift amount = %d" % shift_amount)
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result

# for the value e (in enigma) it shifts -70
def e70_v_decrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        shift_amount = (-1) * ord(keyword[ki])+32-1 
        #print ("decrypt shift amount = %d" % shift_amount)
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result

# This function uses a vigenere cipher to decrypt.
# for the value e (in enigma) it shifts -4
# Can't get it to work, but it does produce results that look like the text in file_012499
def e4_v_decrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        shift_amount = (-1) * ord(keyword[ki])+32+65
        #print ("decrypt shift amount = %d" % shift_amount)
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result

#This function uses a vigenere cipher to decrypt.
# for the value e (in enigma) it shifts -5
def e5_v_decrypt(message, keyword):
    result = ""
    ki=0
    
    for letter in message:
        shift_amount = (-1) * ord(keyword[ki])+32+64
        #print ("decrypt shift amount = %d" % shift_amount)
        result += shift(letter, shift_amount)
        ki += 1
        if ki >= len(keyword):
            ki =0

    return result


# returns a list of text files names in the current directory that match "file_*.txt"
def gettextfilenames():
    listoffiles = []
    import os
    for file in os.listdir("."):
        if file.endswith(".txt") and file.startswith("file_"):
            listoffiles.append(os.path.join(".", file))
    return listoffiles

# reads the given file and returns its contents
def readfile(filename):
    with open(filename, 'r') as f:
        contents = f.read()
        f.close()
    return contents
    
### main program begins

# define a list of common words to look for
common = ["and" , "the", "message", "Message"]
'''
encrypted_message = "2&%*\"TWpt:/f=wSUDEvHg(1Cf+Fg\j`YQr/kJ\0>Rsu{H=.`Gczhc7Hvs61aUL_w@[tNeJ2&O,G'>OIvW:4!`C^1\yCZo@Ij-\KUqH\"hUW\|9i&~q[KDjZ`=y14ZWr$^WN@tuDQjDt3d!s-!eB^*XIB=hy(*sUsuypqm.;4/Nqr\" ~ (!ggs*|vg&|o{\"cmt*ipq{$*[#gmpxwutg $G.Rxt~|(\"o}~m!gy$svu.&x}v5v&x~G.Pu'*Q5nr/lm#\" ~ /!g&'yvrgxxxo.ynt|m.vnt*touz/wm\"ugvo(wu4/Yvs\"ztkkvgx/zp}vu/yv.vnt*R<N4/Wi|p&'oj\"kzt*pou&p*X\I&usts\"k(~m|uo~x(!czwoz.vnpx(XRM=*\vcz/suoik/ri\"\"g/wm\"ugvo(vkjsov.kt#sls0&hy}.eg}*kvgiz*|vg&usts\"k(~m|uo~x{.d /|qujz<mtweqxxo.qt/oiqj&xwiug&$y(}rk}*q#\"o}*i.pk'*|od4/Nw&pr~kl.vnt*q{cmt*i|f&$rm|\"{#o(#jk/lt$ge#~muct~qzorn)8x(\"v\"yo!cs/pz}o&w~|~u@>9owvn%l6qqs>tw|eu~z7pn{ti{#gmpxwutg r\".vu/o!#tgr~(#jk/pq|cr/wm\"ugvo(ttu|*|vg& sk#wxt8(Opj/rm!g-#*i|qzwoz.kt$ozsuzxxo.vnxxo.ch~ |.vnt*^wik}ozs\"ixzpst4=8(Pgip {s\"yt!m!cr/nqthk\"ov#\"ywsn#u&p|m.wytn4.vnt*kvcxpm|st&ss{#toq |wqt/yn.gtr|\"~vks*|szz/s{.o{rr(tng$~m!\"zwkv.yo$r(o\"Ipo{ot&rsxvgx/\"pstk/ktz\"iwkzoezt|{.cxt*{vkl$ol.cs~ v#0&X*vsgjtn(#q&$$xs\"w%s|s\"g/lq#\"s~|m.vk(~(wp&$rq\"\"st}{oik/t}\"v&#y(#jk/mpw/y! i!g&&kt$g&'y}zf&#~i|f&~ |.hu\"*|vky/mq~jk\"ol.vk(~63K>-4k#r}5f79+Y+(mqjxAM"

encrypted = v_encrypt("Message 9. abcdefghijklmnopqrstuvwyxy", "enigma")
print (encrypted)
print (e4_v_decrypt("zwoz.kt$ozsuzxxo.vnxxo.ch~", "enigma"))
'''
   
keyword = "enigma"
# get a list of text files names in the current directory that match "file_*.txt" and start looping over them
alltextfiles = gettextfilenames()
for thisfile in alltextfiles:
    print ("opening" + thisfile)
    encrypted_text = readfile(thisfile)
    #print ("file contents start with:" + encrypted_text[0:20])

 
    #this loop first checks the contents of the file, then checks the contents starting at the next character
    # and then the text, for as many characters as there are in keyword, since we don't know where in the file
    # the encrypted text will begin
    for j in range(len(keyword)):
        print (j)
        # decrypt the contents using method 1
        decrypted_text = e69_v_decrypt(encrypted_text, keyword)
        if has_keyword(decrypted_text, common)== True:
            print("***Found readable text in file using e69:" + thisfile)
            print(decrypted_text)

        # decrypt the contents using method 2
        decrypted_text = e4_v_decrypt(encrypted_text, keyword)
        if has_keyword(decrypted_text, common)== True:
            print("***Found readable text in file using e4:" + thisfile)
            print(decrypted_text)

        # decrypt the contents using method 3
        decrypted_text = e5_v_decrypt(encrypted_text, keyword)
        if has_keyword(decrypted_text, common)== True:
            print("***Found readable text in file using e5:" + thisfile)
            print(decrypted_text)

        # decrypt the contents using method 4
        decrypted_text = e70_v_decrypt(encrypted_text, keyword)
        if has_keyword(decrypted_text, common)== True:
            print("***Found readable text in file using e70:" + thisfile)
            print(decrypted_text[0:20])

        # lop one character off the front of the encrpted text for the next time through the loop
        encrypted_text = encrypted_text[1:]
        
'''

print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
encrypted = encrypted[1:]
print (new_decrypt(encrypted, "enigma"))
'''

'''
for i in range(95):
    decrypted_message = decrypt(encrypted_message, i)
    if has_keyword(decrypted_message, common)== True:
        print(decrypted_message)
        print(i)
'''
#print(unencrypted_message)
#print(encrypted_message)
#print(decrypted_message)

