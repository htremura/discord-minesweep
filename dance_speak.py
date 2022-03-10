import pyperclip
import string

letterlist = string.ascii_uppercase + "1234567890"
jazzystring = ""

boring = input("Gimme text to make dance!\n").upper()
for letter in range(len(boring)):
    if boring[letter] in letterlist:
        jazzystring += ":" + boring[letter] + "_:"
    elif boring[letter] == " ":
        jazzystring += ":__:"
    elif boring[letter] == "?":
        jazzystring += ":QSTN:"
    elif boring[letter] == "@":
        jazzystring += ":AT:"
    elif boring[letter] == "&":
        jazzystring += ":AMPRSND:"
    elif boring[letter] == "$":
        jazzystring += ":DLLR:"
    elif boring[letter] == "!":
        jazzystring += ":BANG:"
    else:
        jazzystring += boring[letter]
pyperclip.copy(jazzystring)
