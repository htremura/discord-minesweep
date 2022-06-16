import pyperclip
import string

jazzystring = ""

boring = input("Gimme text to turn into a minesweeper for Discord!\n").upper()
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
    elif boring[letter] == " ":
        jazzystring += "||:white_large_square:||"
    elif boring[letter] == "💥":
        jazzystring += "||:bomb:||"
    else:
        jazzystring += "\n"

pyperclip.copy(jazzystring)