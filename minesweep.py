import random
import pyperclip

def generate_minefield_from_mine_positions(rows, cols, mine_positions):
    """
    Generate a Minesweeper minefield from explicit mine coordinates.

    Parameters:
        rows (int): Number of rows
        cols (int): Number of columns
        mine_positions (list of (row, col)): Mine coordinates

    Returns:
        minefield (2D list): Numbers and 'B' where bombs are located
    """

    #print(f"DEBUG: generate_minefield_from_mine_positions(rows, cols, mine_positions) CALLED")
    #print(f"DEBUG: rows: {rows}, cols: {cols}, mine_positions: {mine_positions}")

    # Initialize empty minefield
    minefield = [[0 for _ in range(cols)] for _ in range(rows)]

    # Place mines
    for r, c in mine_positions:
        minefield[r][c] = 'B'

        # Increment adjacent cells
        for i in range(max(0, r-1), min(rows, r+2)):
            for j in range(max(0, c-1), min(cols, c+2)):
                if minefield[i][j] != 'B':
                    minefield[i][j] += 1

    return minefield

def generate_minefield_from_mbf_hex(mbf_hex):
    """
    Generate a Minesweeper minefield from provided mbf hex string.

    Parameters:
        mbf_hex (string): mbf hexadecimal string

    Returns:
        minefield (2D list): Numbers and 'B' where bombs are located
    """

    #print(f"DEBUG: generate_minefield_from_mbf_hex(mbf_hex) CALLED")
    #print(f"DEBUG: mbf_hex: {mbf_hex}")

    width, height, mine_positions = parse_mbf_hex(mbf_hex)
    return generate_minefield_from_mine_positions(height, width, mine_positions)

def generate_random_mine_positions(rows, cols, mine_count):
    """
    Generate random unique mine positions.

    Parameters:
        rows (int): Number of rows
        cols (int): Number of columns
        mine_count (int): Number of mines

    Returns:
        mine_positions (list of (row, col)): Random mine coordinates
    """

    #print(f"DEBUG: generate_random_mine_positions(rows, cols, mine_count) CALLED")
    #print(f"DEBUG: rows: {rows}, cols: {cols}, mine_count: {mine_count}")

    all_positions = [(r, c) for r in range(rows) for c in range(cols)]
    return random.sample(all_positions, mine_count)

def print_minefield(minefield):
    """
    Print the minefield in a readable format.
    Parameters:
        minefield (2D list): Grid with indicative numbers and 'B' where bombs are located
    """

    #print(f"DEBUG: print_minefield(minefield) CALLED")
    #print(f"DEBUG: minefield: {minefield}")

    for row in minefield:
        print(' '.join(str(cell) if cell != 0 else '0' for cell in row))

def convert_to_discord(minefield):
    """
    Convert minefield to Discord spoilered message using emotes.
    Parameters:
        minefield (2D list): Grid with indicative numbers and 'B' where bombs are located
    Returns:
        status (list): List of status strings regarding length classification
        discord_string (string): Discord formatted string with emotes
        total_chars (int): Total character count of the discord_string
        total_cells (int): Total number of cells in the minefield
    """
    

    #print(f"DEBUG: convert_to_discord(minefield) CALLED")
    #print(f"DEBUG: minefield: {minefield}")
    
    rows = len(minefield)
    cols = len(minefield[0])
    total_cells = rows * cols
    discord_string = ''
    total_chars = 0
    status = []

    emote_map = {
        1: ':one:', 2: ':two:', 3: ':three:', 4: ':four:',
        5: ':five:', 6: ':six:', 7: ':seven:', 8: ':eight:',
        ' ': ':white_large_square:', 'B': ':bomb:'
    }
    
    # Build the jazzy string
    for row in minefield:
        for cell in row:
            emote = emote_map.get(cell, ':white_large_square:')
            part = f'||{emote}||'
            discord_string += part
            total_chars += len(part)
        discord_string += '\n'
        total_chars += 1
    
    # Length classification

    if total_cells > 99:
        status.append("too_many_emotes")

    if total_chars <= 2000:
        status.append("ok")
    elif total_chars <= 4000:
        status.append("nitro_required")
    else:
        status.append("too_long")

    return (status, discord_string, total_chars, total_cells)

def convert_to_plaintext(minefield):
    """
    Generate plaintext representation of the minefield.

    Parameters:
        minefield (2D list): Grid with indicative numbers and 'B' where bombs are located

    Returns:
        plaintext (string): Plaintext representation of the minefield
    """

    #print(f"DEBUG: convert_to_plaintext(minefield) CALLED")
    #print(f"DEBUG: minefield: {minefield}")

    plaintext = ''
    for row in minefield:
        for cell in row:
            plaintext += f'||`{cell}`||'
        plaintext += '\n'
    return plaintext

def parse_mbf_hex(hex_string):
    """
    Parse mbf hex string into minefield dimensions and mine positions.
    Parameters:
        hex_string (string): mbf hexadecimal string
    Returns:
        width (int): Width of the minefield
        height (int): Height of the minefield
        mine_positions (list of (row, col)): Mine coordinates
    """

    #print(f"DEBUG: parse_mbf_hex(hex_string) CALLED")
    #print(f"DEBUG: hex_string: {hex_string}")
    
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

def minefield_to_rbf_hex(minefield):
    """
    Generate mbf hex string from minefield.

    Parameters:
        minefield (2D list): Grid with indicative numbers and 'B' where bombs are located

    Returns:
        mbf_hex (string): mbf hexadecimal string
    """

    #print(f"DEBUG: minefield_to_rbf_hex(minefield) CALLED")
    #print(f"DEBUG: minefield: {minefield}")

    height = len(minefield)
    width = len(minefield[0])

    # Locate mines
    mine_positions = []
    for r in range(height):
        for c in range(width):
            if minefield[r][c] == 'B':
                mine_positions.append((c, r))   # X, Y

    mines = len(mine_positions)

    # MBF format:
    # WIDTH (1 byte)
    # HEIGHT (1 byte)
    # MINES (2 bytes, big endian)
    # MINE POSITIONS: X Y (2 bytes, each 1 byte)
    output = bytearray()
    output.append(width)
    output.append(height)
    output.append((mines >> 8) & 0xFF)          # high byte
    output.append(mines & 0xFF)                 # low byte

    for x, y in mine_positions:
        output.append(x)
        output.append(y)

    # Convert to spaced hex string for readability
    mbf_hex = " ".join(f"{b:02X}" for b in output)
    return mbf_hex


# Main script

script_generated = input('Do you want this script to generate a Minesweeper board? (y/n): ').strip().lower()

if script_generated in ("y", "yes"):
    # Generate minefield mode
    try:
        cols = int(input('Width / Columns: '))
        if cols < 1:
            raise ValueError('Columns must be at least 1.')
        rows = int(input('Height / Rows: '))
        if rows < 1:
            raise ValueError('Rows must be at least 1.')
        minecount = int(input('Number of mines: '))
        if minecount < 1 or minecount >= rows * cols:
            raise ValueError('Number of mines must be at least 1 and less than total cells.')
        randomized_mine_positions = generate_random_mine_positions(rows, cols, minecount)
        minefield = generate_minefield_from_mine_positions(rows, cols, randomized_mine_positions)

        print('\nGenerated Minesweeper Minefield:\n')

    except Exception as e:
        print('Error:', e)

elif script_generated in ("n", "no"):
    # Parse manual MBF mode
    print('Please input your own minefield manually in hexadecimal MBF format (WIDTH (1BYTE) HEIGHT (1BYTE) MINES (2BYTES) MINE POSITIONS (2 BYTES EACH X Y))\nYou can use a service like https://www.mzrg.com/js/mine/make_board.html')
    hex_string = input("> ").strip()
    try:
        width, height, mine_positions = parse_mbf_hex(hex_string)
        print(f"Width: {width}, Height: {height}, Mines: {len(mine_positions)}")
        
        minefield = generate_minefield_from_mbf_hex(hex_string)
        print("\nParsed Minesweeper Minefield:\n")
        
    except Exception as e:
        print("Error parsing MBF:", e)

else:
    print('Invalid choice. Please enter "y" or "n".')
    exit(1)

print_minefield(minefield)

print("\nGenerated .MBF Hexadecimal Representation:")
mbf_hex = minefield_to_rbf_hex(minefield)
print(f'\n{mbf_hex}\n')

print("Do you want to copy this to your clipboard as:\nA Discord spoilered message using emotes? (d)\nA Discord spoilered message using plaintext? (t)\nA .MBF formatted hexadecimal string? (m)")
output_choice = input("> ").strip().lower()

if output_choice in ("d", "discord"):
    # Discord emote output to clipboard
    status, msg, chars, emotes = convert_to_discord(minefield)
    
    print(f"\nLength {chars}, Emotes {emotes}")
    
    if "too_many_emotes" in status:
        print(f"Too many emotes: ({emotes}>99). Cannot send on Discord.")
    else:
        if "ok" in status:
            print(f"You can send this on Discord without Nitro ({chars} <= 2000 & {emotes} <= 99).")
        elif "nitro_required" in status:
            print(f"Message requires Nitro ({chars} > 2000).")
            nitro = input("Do you have Nitro? (y/n): ").strip().lower()
            if nitro in ("y", "yes"):
                print(f"You can send this on Discord only because you have Nitro ({chars} <= 4000) & {emotes} <= 99).")
            else:
                print(f"You can only send this message with Nitro ({chars} > 4000) & {emotes} <= 99).")
        elif "too_long" in status:
            print(f"Message too long ({chars}>4000). Cannot send even with Nitro.")
        else:
            print("Unknown status.")
    
    
    if "too_many_emotes" in status:
        print("Discord message not copied due to emote constraint.")
        ptexq = input("Convert to plaintext?").strip().lower()
        if ptexq in ("y", "yes"):
            plaintext = convert_to_plaintext(minefield)
            try:
                pyperclip.copy(plaintext)
                print('\nPlaintext format copied to clipboard!\n')
            except Exception:
                print('\nCould not copy to clipboard. Please copy manually:\n')
                print(plaintext)
    elif (("ok" in status) or ("nitro_required" in status)):
        try:
            pyperclip.copy(msg)
            print('\nDiscord format copied to clipboard!\n')
        except Exception:
            print('\nCould not copy to clipboard. Please copy manually:\n')
            print(msg)
    else:
        print("Discord message not copied due to length constraint.")

elif output_choice in ("t", "text"):
    plaintext = convert_to_plaintext(minefield)
    try:
        pyperclip.copy(plaintext)
        print('\nPlaintext format copied to clipboard!\n')
    except Exception:
        print('\nCould not copy to clipboard. Please copy manually:\n')
        print(plaintext)

elif output_choice in ("m", "mbf"):
    # MBF hex output to clipboard
    try:
        pyperclip.copy(mbf_hex)
        print('\n.MBF hexadecimal format copied to clipboard!\n')
    except Exception:
        print('\nCould not copy to clipboard. Please copy manually:\n')
        print(mbf_hex)
else:
    print("Invalid input! Nothing copied to clipboard.")
