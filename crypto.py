import sys
def encrypt(text,s):
    result = ""

    #transverse the plain text
    for i in range(len(text)):
        char = text[i]

        #encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char)+ s - 65) % 26 + 65)

        #Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char)+ s - 97) % 26 + 97)
    return result

#check the above fuction
#add what you want to encrypt
text = str(input('What are you thinking :'))
s = 5
print ("Plain Text  : {}" .format(text))
print ("Shift pattern : {}" .format(str(s)))
print ("Cipher: {}" .format (encrypt(text,s)))

    
