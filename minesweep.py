import pyperclip
import string

jazzystring = ""
notdone = True
pasteloop = True
toolong = False
i = 0

while notdone:
    boring = input("Gimme a line to turn into a minesweeper for Discord!\n").upper()
    if (boring == "S") or (boring == "N") or (boring == "B") or (boring == ""):
        jazzystring = jazzystring[:-1]
        break
    for letter in range(len(boring)):
        if boring[letter] == "1":
            if (i+6+3>2000):
                toolong = True
                break
            jazzystring += "||:one:||"
            i+=6+3
        elif boring[letter] == "2":
            if (i+6+3>2000):
                toolong = True
                break
            jazzystring += "||:two:||"
            i+=6+3
        elif boring[letter] == "3":
            if (i+6+5>2000):
                toolong = True
                break
            jazzystring += "||:three:||"
            i+=6+5
        elif boring[letter] == "4":
            if (i+6+4>2000):
                toolong = True
                break
            jazzystring += "||:four:||"
            i+=6+4
        elif boring[letter] == "5":
            if (i+6+4>2000):
                toolong = True
                break
            jazzystring += "||:five:||"
            i+=6+4
        elif boring[letter] == "6":
            if (i+6+3>2000):
                toolong = True
                break
            jazzystring += "||:six:||"
            i+=6+3
        elif boring[letter] == "7":
            if (i+6+5>2000):
                toolong = True
                break
            jazzystring += "||:seven:||"
            i+=6+5
        elif boring[letter] == "8":
            if (i+6+5>2000):
                toolong = True
                break
            jazzystring += "||:eight:||"
            i+=6+5
        elif boring[letter] == "9":
            if (i+6+4>2000):
                toolong = True
                break
            jazzystring += "||:nine:||"
            i+=6+4
        elif boring[letter] == " ":
            if (i+6+18>2000):
                toolong = True
                break
            jazzystring += "||:white_large_square:||"
            i+=6+18
        elif boring[letter] == "💥":
            if (i+6+4>2000):
                toolong = True
                break
            jazzystring += "||:bomb:||"
            i+=6+4
    if not toolong:
        jazzystring += "\n"
    else:
        print("Too many characters!")
        break

while toolong:
    loopq = input("THIS IS AN ERROR CATCHING LOOP. Are we done pasting? (y/n)").upper()
    if (loopq == "Y") or (loopq == ""):
        toolong = False
print("The letter count is: " + str(i))
pyperclip.copy(jazzystring)