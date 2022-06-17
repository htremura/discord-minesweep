import pyperclip
import string

jazzystring = ""
notdone = True
pasteloop = True
i = 0

while notdone:
    boring = input("Gimme a line to turn into a minesweeper for Discord!\n").upper()
    if (boring == "S") or (boring == "N") or (boring == "B") or (boring == ""):
        jazzystring = jazzystring[:-2]
        break
    for letter in range(len(boring)):
        if boring[letter] == "1":
            if (i+6+3>2000):
                i+=6+3
                break
            jazzystring += "||:one:||"
            i+=6+3
        elif boring[letter] == "2":
            if (i+6+3>2000):
                i+=6+3
                break
            jazzystring += "||:two:||"
            i+=6+3
        elif boring[letter] == "3":
            if (i+6+5>2000):
                i+=6+5
                break
            jazzystring += "||:three:||"
            i+=6+5
        elif boring[letter] == "4":
            if (i+6+4>2000):
                i+=6+4
                break
            jazzystring += "||:four:||"
            i+=6+4
        elif boring[letter] == "5":
            if (i+6+4>2000):
                i+=6+4
                break
            jazzystring += "||:five:||"
            i+=6+4
        elif boring[letter] == "6":
            if (i+6+3>2000):
                i+=6+3
                break
            jazzystring += "||:six:||"
            i+=6+3
        elif boring[letter] == "7":
            if (i+6+5>2000):
                i+=6+5
                break
            jazzystring += "||:seven:||"
            i+=6+5
        elif boring[letter] == "8":
            if (i+6+5>2000):
                i+=6+5
                break
            jazzystring += "||:eight:||"
            i+=6+5
        elif boring[letter] == "9":
            if (i+6+4>2000):
                i+=6+4
                break
            jazzystring += "||:nine:||"
            i+=6+4
        elif boring[letter] == " ":
            if (i+6+18>2000):
                i+=6+18
                break
            jazzystring += "||:white_large_square:||"
            i+=6+18
        elif boring[letter] == "💥":
            if (i+6+4>2000):
                i+=6+4
                break
            jazzystring += "||:bomb:||"
            i+=6+4
    if not (i>2000):
        jazzystring += "\n"
    else:
        print("Too many characters!")
        break

while pasteloop == True:
    loopq = input("Are we done with the pasteloop?").upper()
    if loopq == "Y":
        pasteloop = False
print("The letter count is: " + str(i))
pyperclip.copy(jazzystring)