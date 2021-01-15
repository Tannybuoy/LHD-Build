# Dictionary representing the morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Converter
def encrypt(value):
    outmes=''
    for letter in value:
        if letter==' ':
            # '/' character is used to separate words
            outmes=outmes+"/ "
        else:
            # Dictionary is used. Letters are seprated by a space ' '
            outmes=outmes+MORSE_CODE_DICT[letter]+' '
    print(outmes)

# Executes the main function
if __name__ == '__main__':

    #Takes User Input
    val = input("Enter your message in English: ")

    #Converts User input to upper case
    val=val.upper()

    #Shows user input in upper case
    print(val)

    #Calls encryption function
    encrypt(val)
