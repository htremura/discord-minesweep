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
    rows = len(board)
    cols = len(board[0])
    total_cells = rows * cols
    discord_string = ''
    total_chars = 0

    if total_cells > 99:
        return ("too_many_emotes", discord_string, total_chars, total_cells)

    emote_map = {
        1: ':one:', 2: ':two:', 3: ':three:', 4: ':four:',
        5: ':five:', 6: ':six:', 7: ':seven:', 8: ':eight:',
        9: ':nine:', ' ': ':white_large_square:', 'B': ':bomb:'
    }
    
    # Build the jazzy string
    for row in board:
        for cell in row:
            emote = emote_map.get(cell, ':white_large_square:')
            part = f'||{emote}||'
            discord_string += part
            total_chars += len(part)
        discord_string += '\n'
        total_chars += 1
    
    # Length classification
    if total_chars <= 2000:
        return ("ok", discord_string, total_chars, total_cells)

    if total_chars <= 4000:
        return ("nitro_required", discord_string, total_chars, total_cells)

    return ("too_long", total_chars)

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
script_generated = input('Do you want this script to generate a Minesweeper board? (y/n): ').strip().lower()

if script_generated in ("y", "yes"):
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

    except Exception as e:
        print('Error:', e)

elif script_generated in ("n", "no"):
    # Parse manual MBF mode
    print('Please input your own board manually in hexadecimal MBF format (WIDTH (1BYTE) HEIGHT (1BYTE) MINES (2BYTES) MINE POSITIONS (2 BYTES EACH X Y))\n You can use a service like https://www.mzrg.com/js/mine/make_board.html')
    hex_string = input("> ").strip()
    try:
        width, height, mine_positions = parse_mbf_hex(hex_string)
        print(f"Width: {width}, Height: {height}, Mines: {len(mine_positions)}")
        
        board = generate_board(height, width, len(mine_positions), mine_positions)
        print("\nParsed Board:")
        
    except Exception as e:
        print("Error parsing MBF:", e)
else:
    print('Invalid choice. Please enter "y" or "n".')
    exit(1)

print_board(board)
print(f'\n{board_to_mbf_hex(board)}\n')

discord_minesweeper = input("Do you want to convert this to a discord spoilered board? (y/n): ").strip().lower()
if discord_minesweeper in ("y", "yes"):
    status, msg, chars, emotes = convert_to_discord(board)
    
    print(f"Length {chars}, Emotes {emotes}")
    
    if status == "ok":
        print("You can send this on Discord without Nitro.")

    elif status == "nitro_required":
        print(f"Message requires Nitro (length {chars}, emotes {emotes}).")
        nitro = input("Do you have Nitro? (y/n): ").strip().lower()
        if nitro in ("y", "yes"):
            print("You can send this on Discord only because you have Nitro.")
        else:
            print(f"You cannot send this without Nitro.")

    elif status == "too_many_emotes":
        print(f"Too many emotes: ({emotes}>99). Cannot send on Discord.")

    elif status == "too_long":
        print(f"Message too long ({chars}>4000). Cannot send even with Nitro.")

    else:
        print("Unknown status.")
    
    if status in ("ok", "nitro_required"):
        try:
            pyperclip.copy(msg)
            print('\nDiscord format copied to clipboard!\n')
        except Exception:
            print('\nCould not copy to clipboard. Please copy manually.\n')
    else:
        print("Discord message not generated due to length/emote constraints.")
    
else:
    print("Ok!")
    