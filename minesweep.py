import pyperclip
import string

jazzystring = ""
notdone = True
i = 0

while notdone:
    if i==0:
        boring = input("Gimme a line to turn into a minesweeper for Discord!\n").upper()
    else:
        boring = input().upper
    if (boring[0] == "S") or (boring[0] == "N") or (boring[0] == "B"):
        jazzystring = jazzystring[:-1]
        break
    for letter in range(len(boring)):
        if boring[letter] == "1":
            jazzystring += "||:one:||"
        elif boring[letter] == "2":
            jazzystring += "||:two:||"
        elif boring[letter] == "3":
            jazzystring += "||:three:||"
        elif boring[letter] == "4":
            jazzystring += "||:four:||"
        elif boring[letter] == "5":
            jazzystring += "||:five:||"
        elif boring[letter] == "6":
            jazzystring += "||:six:||"
        elif boring[letter] == "7":
            jazzystring += "||:seven:||"
        elif boring[letter] == "8":
            jazzystring += "||:eight:||"
        elif boring[letter] == "9":
            jazzystring += "||:nine:||"
        elif boring[letter] == " ":
            jazzystring += "||:white_large_square:||"
        elif boring[letter] == "💥":
            jazzystring += "||:bomb:||"
    jazzystring += "\n"

pyperclip.copy(jazzystring)