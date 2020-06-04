sequence = int(input('Pick: \n1. Uppercase \n2. Capitalize \n3. Reverse \n4. Leet \n5. Long-Long \n6. Cipher \n: '))
text = input('Your text to convert? : ')
from pycipher import Caesar
import re

if sequence == 1:
    print(text.upper())

if sequence == 2:
    print(text.capitalize())

if sequence == 3:
    reverse = text[::-1]
    print(reverse)

if sequence == 4:
    replacement = {"A":"4", "E":"3", "G":"6", "I":"1", "O":"0", "S":"5", "T":"7"}
    text = text.upper()
    leet = text.translate(text.maketrans(replacement))
    print(leet)

if sequence == 5:
    text = re.sub("aa", "aaaaa", text)
    text = re.sub("oo", "ooooo", text)
    text = re.sub("ee", "eeeee", text)
    text = re.sub("ii", "iiiii", text)
    print(text)

if sequence == 6:
    cipher = Caesar(key=13).encipher(text)
    print(cipher)