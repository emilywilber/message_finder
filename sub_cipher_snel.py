key      = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result

# read a text file
with open('file_010005.txt', 'r') as f:
    encrypted_message = f.read()
    f.close()

#encrypted_message = "%|A\"`A\"`GP\"\"Y}P`{ACPw`b7G`:XHHAH}`JXZ`J{`\"ZX{{`ZJ`V:AZPw`vP:P7\"`\"JGP`KFY}Y:A\"G`{:JG`*ADAKPOAYa`$z%bj|JGP`82$z%b`YZ`|JGP29`A\"`YH`bHZP:HPZqUY\"PO`KXUFAI`CJFXHZPP:`IJGKXZAH}`K:JSPIZ`PGKFJNAH}`Z|P`l~b/;`\"J{ZVY:P`KFYZ{J:G=`|J\"ZPO`UN`Z|P`$KYIP`$IAPHIP\"`,YUJ:YZJ:N=`YZ`Z|P`^HACP:\"AZN`J{`;YFA{J:HAY=`lP:DPFPN=`AH`Z|P`^HAZPO`$ZYZP\"w`$z%b`A\"`YH`YI:JHNG`{J:`Z|P`$PY:I|`{J:`zBZ:Yq%P::P\"Z:AYF`bHZPFFA}PHIPw`bZ\"`KX:KJ\"P`A\"`ZJ`YHYFNMP`:YOAJ`\"A}HYF\"=`\"PY:I|AH}`{J:`\"A}H\"`J{`PBZ:Y`ZP::P\"Z:AYF`AHZPFFA}PHIP=`YHO`A\"`JHP`J{`GYHN`YIZACAZAP\"`XHOP:ZYDPH`Y\"`KY:Z`J{`$z%bwxPn2B(;G[)(gU"
decrypted_message = decrypt(encrypted_message)



print(encrypted_message)
print(decrypted_message)
