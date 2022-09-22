#johndanaherknowsnothinaboutthehalfguardmate:)
import string
import sys

mode = input("""Do You want to code or decode a message? 
Type 1 for coding 2 for decoding with Brute Force or 3 to quit program: 
""")
if mode == "1":
    plainText = input("Enter Your message here: ")
    shift = int(input("Enter shift key number neede to encryption: "))

    def do_the_encryption(plainText, shift):
        encrypted_message = ""
        for x in plainText:
            if x.isalpha():
                numberInASCII = ord(x)
                numberInASCII += shift

                if x.isupper():
                    if numberInASCII > 90:
                            numberInASCII -= 26
                elif numberInASCII > 122:
                        numberInASCII -= 26
                encrypted_message += chr(numberInASCII)
            else:
                encrypted_message += x

        return encrypted_message
    print(do_the_encryption(plainText,shift))

if mode == "2":
    messageToDecode = input("Paste Your encrypted message here: ")

    def cezar_decryption(messageToDecode, shiftKey):
        decodedText = ""
        for letter in messageToDecode:
            ASCIIcode = ord(letter)
            ASCIIcode += shiftKey
            while ASCIIcode > 122:
                ASCIIcode -= 95
            while ASCIIcode < 32:
                ASCIIcode += 95
            decodedText += chr(ASCIIcode)
        return decodedText

    for shift in range(-50, 50):
        print(cezar_decryption(messageToDecode, shift))

if mode == "3":
    print("Goodbye!")
    sys.exit()
