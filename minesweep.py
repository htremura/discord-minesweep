import pyperclip
import string

jazzy_string = ""
toolong = False
emotes = 0
i = 0

while True:
    boring = input("Gimme a line to turn into a minesweeper for Discord! (Enter an empty string, \"S\", \"N\", or \"B\" to exit)\n").upper()
    if (boring == "S") or (boring == "N") or (boring == "B") or (boring == ""):
        jazzy_string = jazzy_string[:-1]
        break
    for letter in range(len(boring)):
        if boring[letter] == "1":
            if (i+6+3>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:one:||"
            emotes+=1
            i+=6+3
        elif boring[letter] == "2":
            if (i+6+3>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:two:||"
            emotes+=1
            i+=6+3
        elif boring[letter] == "3":
            if (i+6+5>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:three:||"
            emotes+=1
            i+=6+5
        elif boring[letter] == "4":
            if (i+6+4>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:four:||"
            emotes+=1
            i+=6+4
        elif boring[letter] == "5":
            if (i+6+4>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:five:||"
            emotes+=1
            i+=6+4
        elif boring[letter] == "6":
            if (i+6+3>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:six:||"
            emotes+=1
            i+=6+3
        elif boring[letter] == "7":
            if (i+6+5>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:seven:||"
            emotes+=1
            i+=6+5
        elif boring[letter] == "8":
            if (i+6+5>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:eight:||"
            emotes+=1
            i+=6+5
        elif boring[letter] == "9":
            if (i+6+4>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:nine:||"
            emotes+=1
            i+=6+4
        elif boring[letter] == " ":
            if (i+6+18>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:white_large_square:||"
            emotes+=1
            i+=6+18
        elif boring[letter] == "💥":
            if (i+6+4>2000) or (emotes>=99):
                toolong = True
                break
            jazzy_string += "||:bomb:||"
            emotes+=1
            i+=6+4
    if not toolong:
        jazzy_string += "\n"
    else:
        print("\nToo many characters!\n")
        break

while toolong:
    loopq = input("THIS IS AN ERROR CATCHING LOOP. Are we done pasting? (y/n):").upper()
    if (loopq == "Y") or (loopq == ""):
        toolong = False
print("The letter count is: " + str(i) + "\nThe emote count is: " + str(emotes) + "\n")
pyperclip.copy(jazzy_string)