import pyperclip

jazzystring = ""

boring = input("Gimme text to make dance!\n").upper()
for letter in range(len(boring)):
    if boring[letter] == " ":
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
        jazzystring += ":EXCLMTN:"
    elif boring[letter] == ",":
        jazzystring += ",:__:"
    else:
        jazzystring += ":" + boring[letter] + "_:"
pyperclip.copy(jazzystring)
