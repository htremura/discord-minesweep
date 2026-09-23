# discord-minesweep
A python script to generate, import, and convert boards of minesweeper for use in the Discord chat service. Do note that Discord has an emote limit of 99 emotes per message. As such I've found that 11x9 (99 tiles) or 12x8 (96 tiles) grids work well with ~20-23 mines. Output is placed into your clipboard and can then be pasted into Discord.

Requirements:
- Python 3.10 or newer
- pyperclip

Run the script with:
python discord-minesweep.py
