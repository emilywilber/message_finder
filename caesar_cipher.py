def has_keyword(message, keywords):
    message = " " + message

    for word in keywords:
        word = " " + word
        if word in message:
            return True

    return False        
'''
def find_shift(message):
    for i in range(95):
        count = 0
        if count < 95:
            bah = decrypt(message, i)
            if has_keyword(bah, common):
                return decrypt(bah, i)
        count += 1
'''
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

common = ["and" , "the", "message"]

encrypted_message = "vGzr_35;I0pn@MTQH9x%Sf#\it<{ZLw*}]9A3YNXK+g(*(\8qYU.0.8(fQ(8P=0^UYA(bX2`m!advF_>awIW""\8a3F>1j4f$M 8=>&-p37=`KQ9++=79~f~vQ/,9~G535.9:5=up~K*97=0/7,=.6%~5+~*69~=,*~=0:~+;590;9~/8~',5*507~65::90~19++=79+~50~+);6~=~'=%~*6=*~0/~/09r~=.=,*~8,/1~*69~+90:9,~=0:~50*90:9:~,9;5.590*r~+)+.9;*+~*69~9&5+*90;9~/8~*69~19++=79r~=~8/,1~/8~+9;),5*%~*6,/)76~/<+;),5*%p~J69~'/,:~+*97=0/7,=.6%~5+~/8~W,993~/,5750~=0:~19=0+~|;/0;9=29:~',5*507|p~J69~85,+*~,9;/,:9:~)+9~/8~*69~*9,1~'=+~50~mjee~<%~T/6=009+~J,5*6915)+~50~65+~K*97=0/7,=.65=r~=~*,9=*5+9~/0~;,%.*/7,=.6%~=0:~+*97=0/7,=.6%~:5+7)5+9:~=+~=~<//3~/0~1=75;p~W909,=22%r~19++=79+~'522~=..9=,~*/~<9~+/19*6507~92+9d~51=79+r~=,*5;29+r~+6/..507~25+*+r~/,~+/19~/*69,~;/(9,*9&*~=0:r~;2=++5;=22%r~*69~65::90~19++=79~1=%~<9~50~50(5+5<29~503~<9*'990~*69~(5+5<29~2509+~/8~=~.,5(=*9~29**9,p~J69~=:(=0*=79~/8~+*97=0/7,=.6%r~/(9,~;,%.*/7,=.6%~=2/09r~5+~*6=*~19++=79+~:/~0/*~=**,=;*~=**90*5/0~*/~*691+92(9+p~N2=502%~(5+5<29~90;,%.*9:~19++=79+~0/~1=**9,~6/'~)0<,9=3=<29~'522~=,/)+9~+)+.5;5/0r~=0:~1=%~50~*691+92(9+~<9~50;,5150=*507~50~;/)0*,59+~'69,9~90;,%.*5/0~5+~52297=2p~J69,98/,9r~'69,9=+~;,%.*/7,=.6%~.,/*9;*+~*69~;/0*90*+~/8~=~19++=79r~+*97=0/7,=.6%~;=0~<9~+=5:~*/~.,/*9;*~</*6~19++=79+~=0:~;/11)05;=*507~.=,*59+p~K*97=0/7,=.6%~50;2):9+~*69~;/0;9=2190*~/8~508/,1=*5/0~'5*650~;/1.)*9,~8529+p~U0~:575*=2~+*97=0/7,=.6%r~929;*,/05;~;/11)05;=*5/0+~1=%~50;2):9~+*97=0/7,=.65;~;/:507~50+5:9~/8~=~*,=0+./,*~2=%9,r~+);6~=+~=~:/;)190*~8529r~51=79~8529r~.,/7,=1~/,~.,/*/;/2p~Q9:5=~8529+~=,9~5:9=2~8/,~+*97=0/7,=.65;~*,=0+15++5/0~<9;=)+9~/8~*695,~2=,79~+5$9p~]+~=~+51.29~9&=1.29r~=~+90:9,~1576*~+*=,*~'5*6~=0~500/;)/)+~51=79~8529~=0:~=:4)+*~*69~;/2/,~/8~9(9,%~mnn*6~.5&92~*/~;/,,9+./0:~*/~=~29**9,~50~*69~=2.6=<9*r~=~;6=079~+/~+)<*29~*6=*~+/19/09~0/*~+.9;585;=22%~2//3507~8/,~5*~5+~)025392%~*/~0/*5;9~5*payBIoDv3W0_B"
decrypted_message = decrypt(encrypted_message, shift)
for i in range(95):
    shift = i
    if has_keyword(decrypted_message, common)== True:
        decrypted_message = decrypt(encrypted_message, i)

#print(unencrypted_message)
#print(encrypted_message)
print(decrypted_message)




      
