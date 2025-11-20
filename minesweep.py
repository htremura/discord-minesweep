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
    return jazzy_string

def parse_mbf_hex(hex_string):
    # remove spaces/newlines
    cleaned = hex_string.replace(' ', '').replace('\n', '')
    
    if len(cleaned) < 8:
        raise ValueError('Hex string too short to contain MBF header.')

    data = bytes.fromhex(cleaned)

    width  = data[0]
    height = data[1]
    mines  = (data[2] << 8) | data[3]

    expected_len = 4 + mines * 2
    if len(data) != expected_len:
        raise ValueError(f'Expected {expected_len} bytes for {mines} mines, got {len(data)}.')

    mine_positions = []
    idx = 4
    for _ in range(mines):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        # x=column, y=row
        mine_positions.append((y, x))

    return width, height, mine_positions

def board_to_mbf_hex(board):
    height = len(board)
    width = len(board[0])

    # Locate mines
    mine_positions = []
    for r in range(height):
        for c in range(width):
            if board[r][c] == 'B':
                mine_positions.append((c, r))   # X, Y

    mines = len(mine_positions)

    # MBF format:
    # WIDTH (1 byte)
    # HEIGHT (1 byte)
    # MINES (2 bytes, big endian)
    # MINE POSITIONS: X Y (each 1 byte)
    output = bytearray()
    output.append(width)
    output.append(height)
    output.append((mines >> 8) & 0xFF)          # high byte
    output.append(mines & 0xFF)                 # low byte

    for x, y in mine_positions:
        output.append(x)
        output.append(y)

    # Convert to spaced hex string for readability
    return " ".join(f"{b:02X}" for b in output)


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
        print(f'\n{board_to_mbf_hex(board)}\n')
    except Exception as e:
        print('Error:', e)
else:
    print('Please use a service like https://www.mzrg.com/js/mine/make_board.html or input your own board manually in hexadecimal MBF format (WIDTH (1BYTE) HEIGHT (1BYTE) MINES (2BYTES) MINE POSITIONS (2 BYTES EACH X Y))')
    hex_string = input("> ").strip()
    try:
        width, height, mine_positions = parse_mbf_hex(hex_string)
        print(f"Width: {width}, Height: {height}, Mines: {len(mine_positions)}")
        
        board = generate_board(height, width, len(mine_positions), mine_positions)
        print("\nParsed Board:")
        print_board(board)
        
    except Exception as e:
        print("Error parsing MBF:", e)
    print(f'The letter count is: {i}\nThe emote count is: {emotes}\n')

try:
    pyperclip.copy(convert_to_discord(board))
    print('\nDiscord format copied to clipboard!\n')
except Exception:
    print('\nCould not copy to clipboard. Please copy manually.\n')
