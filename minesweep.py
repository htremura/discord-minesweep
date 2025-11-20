import random
import pyperclip

def generate_board(rows, cols, mines):
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    # Place mines
    all_positions = [(r, c) for r in range(rows) for c in range(cols)]
    mine_positions = random.sample(all_positions, mines)
    for r, c in mine_positions:
        board[r][c] = 'B'
        # Increment adjacent cells
        for i in range(max(0, r-1), min(rows, r+2)):
            for j in range(max(0, c-1), min(cols, c+2)):
                if board[i][j] != 'B':
                    board[i][j] += 1
    return board

def print_board(board):
    for row in board:
        print(' '.join(str(cell) if cell != 0 else ' ' for cell in row))

def convert_to_discord(board):
    jazzy_string = ''
    toolong = False
    emotes = 0
    i = 0
    emote_map = {
        1: ':one:', 2: ':two:', 3: ':three:', 4: ':four:',
        5: ':five:', 6: ':six:', 7: ':seven:', 8: ':eight:',
        9: ':nine:', ' ': ':white_large_square:', 'B': ':bomb:'
    }

    for row in board:
        for cell in row:
            emote = emote_map.get(cell, ':white_large_square:')
            cell_length = len(emote)
            if (i + 6 + cell_length > 2000) or (emotes >= 99):
                toolong = True
                break
            jazzy_string += f'||{emote}||'
            emotes += 1
            i += 6 + cell_length
        if not toolong:
            jazzy_string += '\n'
        else:
            if (i + 6 + cell_length > 2000):
                print('\nToo many characters!\n')
            else:
                print('\nToo many emotes!\n')
            break
    print(f'The letter count is: {i}\nThe emote count is: {emotes}\n')
    try:
        pyperclip.copy(jazzy_string)
        print('\nDiscord format copied to clipboard!\n')
    except Exception:
        print('\nCould not copy to clipboard. Please copy manually.\n')

    print('\nDiscord format copied to clipboard!\n')

# Main script
choice = input('Do you want to generate a Minesweeper board? (y/n): ').strip().lower()

if choice == 'y' or choice == '':
    # Generate board mode
    try:
        rows = int(input('Rows: '))
        if rows < 1:
            raise ValueError('Rows must be at least 1.')
        cols = int(input('Columns: '))
        if cols < 1:
            raise ValueError('Columns must be at least 1.')
        mines = int(input('Number of mines: '))
        if mines < 1 or mines >= rows * cols:
            raise ValueError('Number of mines must be at least 1 and less than total cells.')
        board = generate_board(rows, cols, mines)
        print('\nGenerated Minesweeper Board:')
        print_board(board)
        convert_to_discord(board)
    except Exception as e:
        print('Error:', e)
else:
    # Manual input mode
    jazzy_string = ''
    toolong = False
    emotes = 0
    i = 0
    print('Enter each line of the board using 1-8, space for empty, or B for mine:')
    while True:
        line = input('(Enter an empty line to finish): ').upper()
        if line in ('', 'S', 'N', 'B'):
            jazzy_string = jazzy_string.rstrip()
            break
        for char in line:
            if char in '123456789':
                emote = f":{['zero','one','two','three','four','five','six','seven','eight','nine'][int(char)]}:"
            elif char == ' ':
                emote = ':white_large_square:'
            elif char == 'B':
                emote = ':bomb:'
            else:
                continue

            length = len(emote)
            if (i + 6 + length > 2000) or (emotes >= 99):
                toolong = True
                break
            jazzy_string += f'||{emote}||'
            emotes += 1
            i += 6 + length
        if not toolong:
            jazzy_string += '\n'
        else:
            print('\nToo many characters!\n')
            break
    if toolong:
        while True:
            loopq = input('THIS IS AN ERROR CATCHING LOOP. Are we done pasting? (y/n): ').upper()
            if loopq in ('Y', ''):
                break

    print(f'The letter count is: {i}\nThe emote count is: {emotes}\n')
    try:
        pyperclip.copy(jazzy_string)
        print('\nDiscord format copied to clipboard!\n')
    except Exception:
        print('\nCould not copy to clipboard. Please copy manually.\n')
    print('\nDiscord format copied to clipboard!\n')
