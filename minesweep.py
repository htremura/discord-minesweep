import pyperclip
import string

jazzystring = ""
notdone = True
i = 0

while notdone:
    boring = input("Gimme a line to turn into a minesweeper for Discord!\n").upper()
    if (boring[0] == "S") or (boring[0] == "N") or (boring[0] == "B") or (boring == ""):
        jazzystring = jazzystring[:-2]
        break
    for letter in range(len(boring)):
        if boring[letter] == "1":
            if (i+6+3>2000):
                print("Too many characters!")
                break
            jazzystring += "||:one:||"
            i+=6+3
        elif boring[letter] == "2":
            if (i+6+3>2000):
                print("Too many characters!")
                break
            jazzystring += "||:two:||"
            i+=6+3
        elif boring[letter] == "3":
            if (i+6+5>2000):
                print("Too many characters!")
                break
            jazzystring += "||:three:||"
            i+=6+5
        elif boring[letter] == "4":
            if (i+6+4>2000):
                print("Too many characters!")
                break
            jazzystring += "||:four:||"
            i+=6+4
        elif boring[letter] == "5":
            if (i+6+4>2000):
                print("Too many characters!")
                break
            jazzystring += "||:five:||"
            i+=6+4
        elif boring[letter] == "6":
            if (i+6+3>2000):
                print("Too many characters!")
                break
            jazzystring += "||:six:||"
            i+=6+3
        elif boring[letter] == "7":
            if (i+6+5>2000):
                print("Too many characters!")
                break
            jazzystring += "||:seven:||"
            i+=6+5
        elif boring[letter] == "8":
            if (i+6+5>2000):
                print("Too many characters!")
                break
            jazzystring += "||:eight:||"
            i+=6+5
        elif boring[letter] == "9":
            if (i+6+4>2000):
                print("Too many characters!")
                break
            jazzystring += "||:nine:||"
            i+=6+4
        elif boring[letter] == " ":
            if (i+6+18>2000):
                print("Too many characters!")
                break
            jazzystring += "||:white_large_square:||"
            i+=6+18
        elif boring[letter] == "💥":
            if (i+6+4>2000):
                print("Too many characters!")
                break
            jazzystring += "||:bomb:||"
            i+=6+4
    jazzystring += "\n"
    i+=1

pyperclip.copy(jazzystring)