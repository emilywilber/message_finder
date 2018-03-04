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


common = ["and" , "the", "message"]

encrypted_message = "wawF{4VImevOr}]T dMv+,6B,6B0(66$*(BEYPBv+(Be$(6$5B&,3+(5B0$'(B0(B7+,1.B2)B7+,6B0(025$%/(B',$/2*B,1B7+(B&/$66,&B029,(NBd,//B$1'Bv('I6Bg;&(//(17Bc'9(1785(PBd,//\Bo5PBt<$1NB%()25(B<28B6$<B$1<7+,1*NB0<B',67,1*8,6+('B&2//($*8(Bv('B$1'BkB:,6+B72B(;35(66B72B<28B285B7+$1.6B)25B$//B7+(B7+,1*6B:(B+$9(B/($51('B,1B<285B&/$66PBo5PBt<$1\Bc1'B:+$7B+$9(B<28B/($51('aBd,//\By(B+$9(NB8+NB:(I9(B/($51('B7+$7B7+(B:25/'B+$6B$B*5($7B+,6725<PBv('\B{(6NB$1'B7+$7B7+$1.6B72B/($'(56B68&+B$6Bi(1*+,6Bm+$1NBl2$1B2)Bc5&NB$1'Bu2&5$7,&Bo(7+2'NB7+(B:25/'B,6B)8//B2)B+,6725<PBo5PBt<$1\Bk7B6((06B72B0(B7+$7B7+(B21/<B7+,1*B<28B+$9(B/($51('B,6B7+$7Be$(6$5B:$6B$B6$/$'B'5(66,1*B'8'(PBd,//NBv('NB7+,6B,6B5($//<B48,7(B6,03/(PB{28B+$9(B)/81.('B(9(5<B6(&7,21B2)B7+,6B&/$66PBp2:B81/(66B<28B*(7B$1BcMB21B<285B),1$/B25$/B5(3257B7202552:NB*8<6NBkB+$9(B12B&+2,&(B%87B72B)/81.B7+(B%27+B2)B<28PBf2B<28B81'(567$1'aBd27+\B{(6B6,5PBJq876,'(B7+(Bu&+22/KBv('\Bd,//NB:+$7B$5(B:(B683326('B72B.12:B)25B285B5(3257aBd,//\BkI0B127B685(PBq1(B7+,1*BkB.12:B,6B7+$7Bl2$1B2)Bc5&B,6B127Bp2$+I6B:,)(PBv('\By(//B7+(1B:+2B,6Bp2$+I6B:,)(aGHn6i$qb 65a[z!"


for i in range(95):
    decrypted_message = decrypt(encrypted_message, i)
    if has_keyword(decrypted_message, common)== True:
        print(decrypted_message)
        print(i)
#print(unencrypted_message)
#print(encrypted_message)
#print(decrypted_message)

