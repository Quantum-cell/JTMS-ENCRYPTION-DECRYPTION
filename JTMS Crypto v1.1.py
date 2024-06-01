demo_mode = 0

# module imports
import random
import sys
import textwrap
import shutil

# Enabling text wrap for printed messages
def wrap_text_to_terminal_width(text, width=None):
    if width is None:
        width = shutil.get_terminal_size().columns
    
    wrapper = textwrap.TextWrapper(width=width)
    
    # Split the text into lines
    lines = text.split('\n')
    
    # Wrap each line individually and preserve newlines
    wrapped_lines = [wrapper.fill(line) for line in lines]
    
    # Join the wrapped lines with newline characters
    wrapped_text = '\n'.join(wrapped_lines)
    return wrapped_text

# Welcome Message Section
# Displaying a welcome message to the user upon running the program to enhance user experience.
# The jauntily janky styled welcome message includes ASCII art and instructions for the user.

welcome_message = """
       ⋮░
       ⋮░▄≣≣    ░ ⋮ ｡            ░▄≣    ░
      ▝██▙██▀▒ ▉█████▟▓⋮ ▟██▄▔▄███▒ ▄██▀█▄  TM
        ▒ ▒█▓∵ ▒▓ ▓█▓▒   ▒██｡███▀ ██▒▒██  ▒░ ⋮
        ░ ░██｡  ▒  ██░ ▒░ ▓██ ▒██ ▓██░▜▓██▄ ░ 
     ≣▒▓██▄██▓  ░ ▓██▉ ░  ▒█▓  ░ ▒██  ▄ ｡▓█▓▒
      ░ ▓█▉█▒  ░  ▒██▒ ░  ▒⬛▒   ░▓█▒▒▓███▓▒▒
        ▒▓▒▒░  ░  ▒▓░░  ▔ ░ ▒░   ░  ░▒ ▒▓▓▒▒ ░
        ▒ ░▒░      ≣░   ▔ ░  ░   ░  ░░ ░▒  ░ ░
        ░ ░ ░▔   ⋮░     ⋮ ░  ≣   ░   ░  ░  ░ ｡︎ 
      ░ ░  ▔░     ░     ▔    ░   ░         ░ ｡ 
      ▒    ▔░          ░         ≣          ≣  
        ▒   ░          ░▔        ▒             ▒⋮︎              
  𝓦ELC0ME T⍜ THƸ JTMS ENCЯYPTiON/D𝑬CRYPTI⚬N 𝕄ACHᴉNΞ
   ░       ▔        ░▒   ░          ░░｡          ⋮ 
  """
print(welcome_message)
print()
print(wrap_text_to_terminal_width("Press R to read about what type of characters your message can contain before being encrypted"))
print()
choice = input("Do you wish to (E)ncrypt a message or (D)ecrypt a JTMS code? ").strip().upper()
print()
#============READ ME TEXT CODE==============
# Providing detailed information to users about the program's functionality and limitations.
# Users can read this information to understand what type of messages can be encrypted and any specific instructions or considerations.

Read_me1 = """_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*__*_*_*_*_*_*_*_*_*_*_

This program is designed to encrypt natural conversational text.
The mechanics of this program were inspired by those horrible little plastic tile puzzle toys you get in kids party bags.
For ease of implementation, rather than sliding a tile into a blank space, we use the perspective that we are sliding/swaping the blank space itself.
This should hopefully become more clear if you want to look through the code.


Note: This tool is currently in the Beta-testing phase. As a result, there are some limitations to its functionality. Users are encouraged to report any bugs or provide feedback.


Input Constraints & Warnings: Messages being encrypted should be composed of the ISO basic English alphabet, including lowercase and uppercase letters, the basic latin numerical digits 0 to 9, spaces and basic punctuation.
Scrambling very short messages, a string of only a few characters or a wholly numerical string, or SHOUTING YOUR WHOLE MESSAGE IN CAPSLOCK will betray elements of the encryption method.


Symbol Usage (both yours and this programs): Please restrict your use of symbols to those found on a standard keyboard.

The encryption process will replace non-breaking spaces, zero-width spaces and tabs with regular spaces (U+0020).

Unicode Characters: Your encrypted message will include some Unicode characters. These symbols serve to:
• Mark the placement of spaces and line breaks in the original and decrypted messages.
• Obfuscate the case (uppercase and lowercase) of letters.
• Provide an appearance of containing alternative/additional secrets.
Please make sure that any communication method used to transmit your message supports these characters.

"""

Read_me2 = """

The following Unicode characters are used in the encryption:

Circled Latin Small Letters: ⓐ, ⓑ, ⓒ,... ⓩ (U+24D0 to U+24E9)
Circled Latin Capital Letters: Ⓐ, Ⓑ, Ⓒ,... Ⓩ (U+24B6 to U+24CF)
Squared Latin Capital Letters: 🄰, 🄱, 🄲,... 🅉 (U+1F130 to U+1F149)
Circled Digits: ①, ②, ③,... ⓪ (U+2460 to U+2469)
Negative Circled Latin Capital Letters: 🅐, 🅑, 🅒,... 🅙 (U+1F150 to U+1F159) 
█ (Full Block): (U+2588)
¶ (Pilcrow Sign): U+00B6 
§ (Section Sign): U+00A7
¦ (Broken Vertical Bar): U+00A6 
† (Dagger): U+2020
‡ (Double Dagger): U+2021 
• (Bullet): U+2022
ƒ (Latin Small Letter F With Hook): U+0192 
◊ (Lozenge): U+25CA
‹ (Single Left-Pointing Angle Quotation Mark): U+2039 
‼ (Double Exclamation Mark): U+203C
‽ (Interrobang): U+203D 
… (Horizontal Ellipsis): U+2026
¿ (Inverted Question Mark): U+00BF 
¤ (Currency Sign): U+00A4
› (Single Right-Pointing Angle Quotation Mark): U+203A 
с (Cyrillic Small Letter Es): U+0441
« (Left-Pointing Double Angle Quotation Mark): U+00AB 
һ (Cyrillic Small Letter Shha): U+04BB
і (Cyrillic Small Letter Byelorussian-Ukrainian I): U+0456 
ј (Cyrillic Small Letter Je): U+0458
р (Cyrillic Small Letter Er): U+0440 


"""

Read_me3 = """

In both the Automatic Scrambling and Custom Scrambling modes, users will be asked to nominate a scrambling grid size.
Details of this grid-size choice will be embedded into the encrypted message.

Automatic Scrambling: This algorithm has been developed to give your message a strong shuffling.

Demo Mode: The first line of code in this file is "demo_mode = 0". Modifying this variable to 1 will activate a feature where the scrambling grid is printed onscreen for each movement prescribed by the autolock algorithm. This allows the user to review the swapping of characters in the grid. This mode will be considerably slower than regular use of this program.

Manual Scrambling: Users can input their own scrambling pattern, which will be printed when they end the manual encryption mode.
Do not send this pattern alongside your encrypted message, as this will compromise the security of the encryption.
This has been set up for users who want to pre-establish a personal lock/unlock algorithm with their reader.
Any such algorithms should take variable grid sizes into account:
locking a 23*19 grid with a pattern that worked fine for a 7*4 grid will leave much of the grid unscrambled, reducing security.

While the manual encrypt function is available, its usage is limited, and anyone wanting to develop a personal lock/unlock algorithm would be best to consider editing the automatic shuffling pattern, saved in the snake_pattern_seq() function. 

Have Fun!

"""
    
# initialising grid variables

GridHeight = 0
GridLength = 0


#============ENCRYPTION CODE DEFINITIONS==============

def spaceless_words(s):

# The following is an elaborate way of marking where spaces and uppercase letters are in the input message, responsibly removing the spaces.
# Replacements used rather than a dictionary for speed optimisation and readability of the replacement categories.

    s = s.replace('\xa0', ' ')  # Replace non-breaking spaces
    s = s.replace('\t', ' ')  # Replace tabs
    s = s.replace('\n', 'с')  # Replace newlines. This is the first of 5 occasions certain Cyrillic characters are used because of their similarity to Latin letters. 
    s = s.replace('\u200B', ' ')  # Replace zero-width spaces

    # Step 1 - if a capital letter is preceded by a space, replace with Circled Latin Small Letters 
    s = s.replace(' A', 'ⓐ').replace(' B', 'ⓑ').replace(' C', 'ⓒ').replace(' D', 'ⓓ').replace(' E', 'ⓔ') \
         .replace(' F', 'ⓕ').replace(' G', 'ⓖ').replace(' H', 'ⓗ').replace(' I', 'ⓘ').replace(' J', 'ⓙ') \
         .replace(' K', 'ⓚ').replace(' L', 'ⓛ').replace(' M', 'ⓜ').replace(' N', 'ⓝ').replace(' O', 'ⓞ') \
         .replace(' P', 'ⓟ').replace(' Q', 'ⓠ').replace(' R', 'ⓡ').replace(' S', 'ⓢ').replace(' T', 'ⓣ') \
         .replace(' U', 'ⓤ').replace(' V', 'ⓥ').replace(' W', 'ⓦ').replace(' X', 'ⓧ').replace(' Y', 'ⓨ') \
         .replace(' Z', 'ⓩ')

    # Step 2 - if a capital letter is NOT preceded by a space, replace with Circled Latin Capital Letters 
    s = s.replace('A', 'Ⓐ').replace('B', 'Ⓑ').replace('C', 'Ⓒ').replace('D', 'Ⓓ').replace('E', 'Ⓔ') \
         .replace('F', 'Ⓕ').replace('G', 'Ⓖ').replace('H', 'Ⓗ').replace('I', 'Ⓘ').replace('J', 'Ⓙ') \
         .replace('K', 'Ⓚ').replace('L', 'Ⓛ').replace('M', 'Ⓜ').replace('N', 'Ⓝ').replace('O', 'Ⓞ') \
         .replace('P', 'Ⓟ').replace('Q', 'Ⓠ').replace('R', 'Ⓡ').replace('S', 'Ⓢ').replace('T', 'Ⓣ') \
         .replace('U', 'Ⓤ').replace('V', 'Ⓥ').replace('W', 'Ⓦ').replace('X', 'Ⓧ').replace('Y', 'Ⓨ') \
         .replace('Z', 'Ⓩ')

    # Step 3 - if a lowercase letter is preceded by a space, replace with Squared Latin Capital Letters 
    s = s.replace(' a', '🄰').replace(' b', '🄱').replace(' c', '🄲').replace(' d', '🄳').replace(' e', '🄴') \
         .replace(' f', '🄵').replace(' g', '🄶').replace(' h', '🄷').replace(' i', '🄸').replace(' j', '🄹') \
         .replace(' k', '🄺').replace(' l', '🄻').replace(' m', '🄼').replace(' n', '🄽').replace(' o', '🄾') \
         .replace(' p', '🄿').replace(' q', '🅀').replace(' r', '🅁').replace(' s', '🅂').replace(' t', '🅃') \
         .replace(' u', '🅄').replace(' v', '🅅').replace(' w', '🅆').replace(' x', '🅇').replace(' y', '🅈') \
         .replace(' z', '🅉')

    
    # Step 4 - if a number is preceded by a space, replace it with Circled Digits 
    s = s.replace(' 1', '①').replace(' 2', '②').replace(' 3', '③').replace(' 4', '④').replace(' 5', '⑤') \
         .replace(' 6', '⑥').replace(' 7', '⑦').replace(' 8', '⑧').replace(' 9', '⑨').replace(' 0', '⓪')

    # Step 5 - similar treatment for spaces preceding a symbol
    #          In regular conversational text, as the read_me asks users to stick with, some of these may be unlikely, but it's best to be careful. 
    s = s.replace(' !', '🅐').replace(' "', '🅑').replace(' £', '🅒').replace(' $', '🅓').replace(' %', '🅔') \
         .replace(' ^', '🅕').replace(' &', '🅖').replace(' *', '🅗').replace(' (', '🅘').replace(' )', '🅙') \
         .replace(' \\', '¤').replace(' /', '¶').replace(' ;', '§').replace(' :', '¦').replace(" '", '†') \
         .replace(' @', '‡').replace(' #', '•').replace(' ~', '◊').replace(' [', '‹').replace(' {', '›') \
         .replace(' ]', '‼').replace(' }', '‽').replace(' -', 'ƒ').replace(' _', '«').replace(' =', '…') \
         .replace(' +', '¿').replace(' *', '×')

    
    # Step 6 - probably shouldn't have to do this if the above worked, and the user didn't add anything funky to their input,
    # but replace remaining spaces with Cyrillic Small Letter Je. 
    s = s.replace(' ', 'ј')


    return s


def userinput():

#   This and the following 4 functions collects the users message to be encrypted and arranges it into a grid.

#   The grid will have a blank space (█) in the top left grid space, and a 'һ' filler (discussed below) if necessary.

#   If the length of the message plus the █ is a prime number, 'һ' is added to ensure a grid with more than 1 row is possible.

#   This symbol is not a lowercase H, is is һ, the Cyrillic Small Letter Shha, unicode U+04BB


    global GridHeight, GridLength
    print("Enter your message (type 'END' on a new line to finish):")

    input_lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        input_lines.append(line)

    input_message = "\n".join(input_lines)
    input_message=str(input_message)
    spacelessd_message = spaceless_words(input_message)
    
    # the following lines add a 'һ' to the message if the length +1 is prime.
    # It has not yet been determined how effective a shuffling grid with only 2 rows or 2 columns might be compared to deeper/thicker grids.
    # Further consideration will be given to only offering grids with 3 or more rows and 3 or more columns.
    
    if len(spacelessd_message) > 2 and len(find_factors(len(spacelessd_message)+1)) == 2:
        spacelessd_message += "һ"
    num_characters = len(spacelessd_message)+1
    print()

    # The following lines of code provide the user with grid size options, using the following 2 functions. 
    print()
    grid_options = generate_grid_options(num_characters)
    print("Grid options:")
    for i, option in enumerate(grid_options):
        print(f"{chr(97 + i)} = {option[0]} * {option[1]}")
    print()
    
    while True:
        choice = input("Choose a grid option: ").strip().lower()
        print()
        if choice and choice.isalpha() and choice in map(chr, range(97, 97 + len(grid_options))):
            chosen_option = grid_options[ord(choice) - 97]
            GridHeight, GridLength = chosen_option
            print(f"Grid sizes chosen: {GridHeight} x {GridLength}")
            break
        else:
            print("Invalid choice. Please choose a valid grid option.")

    
    return spacelessd_message

def find_factors(number): # factors of the length of the message plus █ and 'һ' if it was added.
    
    #  Args: number (int): The number for which factors are to be found.
    #  Returns: list: A list of factors of the given number.
    
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def generate_grid_options(num_characters):  # Generates valid grid options based on the number of characters in the message.

    #  Args:  num_characters (int): The number of characters in the message.
    #  Returns: list: A list of tuples representing valid grid options.
    
    factors = find_factors(num_characters)
    options = []
    for i in range(len(factors) // 2):
        width = factors[i]
        height = factors[-i - 1]
        if width != 1 and height != 1:  # Exclude options with one dimension as 1
            option = (width, height)
            options.append(option)
            # Add option with width and height swapped
            options.append((height, width))
    
    # Include square numbers as valid options
    if len(factors) % 2 != 0:
        square_root = int(num_characters ** 0.5)
        if square_root * square_root == num_characters:
            options.append((square_root, square_root))
    
    return options



def create_grid(elements):  #Creates a grid based on the elements provided.

    # Args: elements (list): A list of elements to be placed in the grid.
    # Returns: list: A 2D list representing the grid.

    grid = [[""] * GridLength for _ in range(GridHeight)]
    element_index = 0
    # Insert the '█' tile at the top left corner
    grid[0][0] = "█"
    # Insert the elements starting from the first row and first column
    for i in range(GridHeight):
        for j in range(GridLength):
            if i != 0 or j != 0:  # Skip the first cell where '█' is placed
                if element_index < len(elements):
                    grid[i][j] = elements[element_index]
                    element_index += 1
                else:
                    # If we run out of elements, fill the remaining cells with an empty string
                    grid[i][j] = ""
    return grid


def print_grid(grid):

    #  Args: The function takes a single argument, grid, which is a 2D list representing the grid.
    #  Returns: The function doesn't return anything (None).
    
    for row in grid:
        # Print each element of the row without line breaks
        print("".join(str(x) if x != 0 else "█" for x in row))


def swap_blank(grid, direction):

    #  Swapping the █ with adjacent grid elements
    #  Directions will be determined by functions to follow.

    #  Args: It takes two arguments, grid, a 2D list representing the grid, and direction, a string representing the direction in which to move the blank space.
    #  Returns: It returns a boolean value (True if the blank space was successfully moved, False otherwise).
    global GridHeight, GridLength
    blank_i, blank_j = 0, 0  # Initialize blank space coordinates
    for i in range(GridHeight):  # Find blank space in grid
        for j in range(GridLength):
            if grid[i][j] == "█":
                blank_i, blank_j = i, j
                break
        else:
            continue
        break

    # Check if the direction input is empty
    if len(direction) == 0:
        print()
        print("Invalid move! Direction input cannot be empty.")
        print()
        return False

    if direction[0].strip().upper() == "U":
        if blank_i == 0:  # Check if blank space is in top row
            return False
        grid[blank_i][blank_j] = grid[blank_i - 1][blank_j]
        grid[blank_i - 1][blank_j] = "█"  # Preserve '█' in the new position
    elif direction[0].strip().upper() == "D": 
        if blank_i == GridHeight - 1:  # Check if blank space is in bottom row
            return False
        grid[blank_i][blank_j] = grid[blank_i + 1][blank_j]
        grid[blank_i + 1][blank_j] = "█"  # Preserve '█' in the new position
    elif direction[0].strip().upper() == "L": 
        if blank_j == 0:  # Check if blank space is in leftmost column
            return False
        grid[blank_i][blank_j] = grid[blank_i][blank_j - 1]
        grid[blank_i][blank_j - 1] = "█"  # Preserve '█' in the new position
    elif direction[0].strip().upper() == "R":
        if blank_j == GridLength - 1:  # Check if blank space is in rightmost column
            return False
        grid[blank_i][blank_j] = grid[blank_i][blank_j + 1]
        grid[blank_i][blank_j + 1] = "█"  # Preserve '█' in the new position
    else:
        print()
        print("Invalid move! Please enter a valid direction ")
        print("[U]p, [D]own, [L]eft, [R]ight, [end].")
        print()
        return False
    
    return True

    return True


# functions to insert details of the grid and scrambling method into the encrypted message

def insert_character(original_string, character, position):

    # Args: original_string (str): The original string where the character will be inserted.
         #  character (str): The character to insert into the string.
         #  position (int): The position at which to insert the character in the string.
         
    # Returns: str: The modified string with the character inserted at the specified position.
   
    return original_string[:position-1] + character + original_string[position-1:]

def number_to_letter(number):
    
    # Convert a number to a corresponding ASCII character.
    
    # Args: number (int): The number to be converted to a corresponding ASCII character.
    # Returns: str: The ASCII character corresponding to the input number.

    return chr(number + 96)  # Offset by 96 to convert the 1st 26 numbers to ASCII value of lowercase letters. 



def manualslide():
# custom shuffling
    print(wrap_text_to_terminal_width("You chose option B - Manual Sliding. The sliding pattern you generate will be printed along with your encrypted message."))
    print()
    print("Type 'end' when you have finished your sliding pattern")
    print()
    global GridHeight, GridLength
    elements = userinput()
    grid = create_grid(elements)
    print_grid(grid)
    move_sequence = ""  # Initialize an empty string to store the move sequence
    while True:
        print()
        direction = input("Enter a direction to move [U]p, [D]own, [L]eft, [R]ight, [end].: ")
        print()
        if direction == 'end':
            break  # Exit the loop if the user inputs 'end'
        if swap_blank(grid, direction):  # Check if the move is valid
            move_sequence += direction[0]  # Append the first character of the direction to the move sequence
            print_grid(grid)  # Print the updated state of the grid after each valid move
        else:
            print()
            print("Invalid move!")  # If move is invalid, notify the user
            print()
            
    print("Move sequence:", move_sequence)  # Print the final move sequence
    
    # Create a string to store the combination of characters in each row
    combined_row = "" # initialise empty combined_row string
    for row in grid: # read grid off row by row into combined_row
        for char in row:
            combined_row += str(char)  # Convert integers to strings before concatenating

    # Hiding the grid size & shuffling option in the encryption
    combined_row=insert_character(combined_row,number_to_letter(GridHeight),7)
    combined_row=insert_character(combined_row,number_to_letter(GridLength),11)
    combined_row=insert_character(combined_row, 'і', random.randint(12, len(combined_row)))
    # the Cyrillic symbol і is stashed randomly in the encrypted message to indicate manual sliding was used.
    print("encrypted text: ")

    # # hide █ as its appearance might give a clue as to its function
    # р is the Cyrillic Small Letter Er, unicode U+0440
    combined_row=combined_row.replace('█', 'р')

    
    print(combined_row)

def snake_pattern_seq(height, width):
    
# Auto-shuffle algorithm - the "empty space" █ swaps with adjacent characters in the following movement patterns:

#  PART ONE -- Always starting at the top left, █ swaps all the way to bottom row, goes right, all the way to the top,
#  ▔▔▔▔▔▔▔▔▔    right, bottom, right, and so on depending on grid_width, producing a vertical snaking pattern. 
#
#    EVEN AMOUNT OF COLUMNS             ODD AMOUNT OF COLUMNS
#    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔            ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
#     start┌┐┌┐┌‖┐┌┐┌┐end               start┌┐┌┐‖┐┌┐┌┐
#         ││││││‖││││││                     │││││‖│││││
#        ======= ========                   ====== ======
#         ││││││‖││││││                     │││││‖│││││
#         └┘└┘└┘‖└┘└┘└┘                     └┘└┘└‖└┘└┘end


#  PART TWO -- The starting point of Part Two is where Part One left the █, always on the righthand column. 
#  ▔▔▔▔▔▔▔▔▔    The █ will swap in one of two horizontal snaking patterns back to the leftmost column.
#
#  STARTING AT TOP RIGHT, EVEN # OF ROWS    STARTING AT BOTTOM RIGHT, EVEN # OF ROWS
#  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
#         ┌──────‖──────START                        ┌──────‖──────END
#         └──────‖──────┐                            └──────‖──────┐
#       =========  ==========                      ==========  =========
#         ┌──────‖──────┘                            ┌──────‖──────┘
#         └──────‖──────END                          └──────‖──────START
#
#
#  STARTING AT TOP RIGHT, ODD # OF ROWS    STARTING AT BOTTOM RIGHT, ODD # OF ROWS
#  ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔    ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
#         ┌──────‖──────START                      END──────‖──────┐
#         └──────‖──────┐                            ┌──────‖──────┘
#         ┌──────‖──────┘                            └──────‖──────┐
#       =========  =========                       ==========  ==========    
#         └──────‖──────┐                            ┌──────‖──────┘
#       END──────‖──────┘                            └──────‖──────START


    pattern = ""

# ===PART ONE===
    # Initial horizontal snaking through columns - starting with a down movement 
    for i in range(width):
        if i % 2 == 0:  # If the column index is even, go down
            pattern += "D" * (height - 1)
        else:  # If the column index is odd, go up
            pattern += "U" * (height - 1)
        if i != width - 1:  # Don't add a right move after the last column
            pattern += "R"

# ===PART TWO===
    # Add moves to go all the way left
    pattern += "L" * (width - 1)

    # Determine the final position after Part One
    if width % 2 == 0:
        final_row = "top"
    else:
        final_row = "bottom"

    # If the snake ends at the top after pt1    
    if final_row == "top":
        pattern += "D"  # Move down
        for i in range(height - 1):
            if i % 2 == 0:  # If the row index is even, go right
                pattern += "R" * (width - 1)
            else:  # If the column index is odd, go left
                pattern += "L" * (width - 1)
            if i != height - 1:
                pattern += "D" 
        
    # If the snake ends at the bottom after pt1
    else:  
        pattern += "U"  # Move up
        for i in range(height - 1):
            if i % 2 == 0:  # If the row index is even, go right
                pattern += "R" * (width - 1)
            else:  # If the column index is odd, go left
                pattern += "L" * (width - 1)
            if i != height - 1:
                pattern += "U" 
    # Our pattern will have an extra D or U at the end. In the encryption it won't cause any problems as it will just be ignored as an invalid move.
    # However, we will use this pattern in the decryption part of this program, and the extra move will be valid and will cause issues if it isn't removed.
    pattern = pattern = pattern[:-1]
    return pattern

def autoslide(elements):
# Passing the auto-shuffle algorithm to the swap_blank() function 

    grid = create_grid(elements)
        
    pattern = snake_pattern_seq(GridHeight, GridLength)

    move_sequence = ""
    for movement in pattern:  
        if movement == 'U':
            swap_blank(grid, "up")
            move_sequence += "U"
        elif movement == 'D':
            swap_blank(grid, "down")
            move_sequence += "D"
        elif movement == 'L':
            swap_blank(grid, "left")
            move_sequence += "L"
        elif movement == 'R':
            swap_blank(grid, "right")
            move_sequence += "R"
        if demo_mode == 1:
            print_grid(grid)  # Print the updated state of the grid after each move
   
    combined_row = "" # initialise empty combined_row string
    for row in grid:  # read grid off row by row into combined_row
        for char in row:
            combined_row += str(char) # Convert integers to strings before concatenating
    # Hiding the grid size & shuffling option in the encryption
    combined_row = insert_character(combined_row, number_to_letter(GridHeight), 7)
    combined_row = insert_character(combined_row, number_to_letter(GridLength), 11)

    combined_row=combined_row.replace('█', 'р') # hide █
    if choice == 'E':
        print()
        print("encrypted text: ")
        print()
        print(combined_row)
        print()
    return move_sequence

def slidingchoice(): # self-explanitory
    global choice2
    choice2 = input("Do you want to use automatic sliding patterns (A) or key in your own moves (B)? (A/B): ").strip().upper()
    
    if choice2 == 'A':
        print("You chose option A - Automatic Sliding.")
        print()
        elements = userinput()
        autoslide(elements)
    elif choice2 == 'B':
        manualslide()
    else:
        print("Invalid choice. Please select either A or B.")
        slidingchoice()

#============ END OF ENCRYPTION CODE DEFINITIONS==============


#============DECRYPTION CODE DEFINITIONS==============

def collect_encryption():
#  Collects the encrypted message and removes any superfluous spaces that might have accidentally been added to it. 
    global encrypted_message
    print()
    encrypted_message = input("Please paste your JTMS encrypted message: ").strip()
    return encrypted_message

def letter_to_number(letter):  #  Conversion of letters to their ASCII code.
    return ord(letter) - 96

def define_grid(encrypted_message):  #  Collect & translate grid dimension characters from encrypted message. 
    global grid_height, grid_width  
    grid_height = letter_to_number(encrypted_message[6])
    grid_width = letter_to_number(encrypted_message[10])

    encrypted_message = encrypted_message[:6] + encrypted_message[7:]
    encrypted_message = encrypted_message[:9] + encrypted_message[10:]
    encrypted_message = encrypted_message.replace('р', '█')  #  Reinstate the good old █

    print(f"Grid Height: {grid_height}")
    print(f"Grid Width: {grid_width}")

    return grid_height, grid_width, encrypted_message

def detect_shuffle(encrypted_message):  #  Detect if encrypted message was manually or automatically scrambled. 
    if 'і' in encrypted_message:
        encrypted_message = encrypted_message.replace('і', '')
        #  Remove indication of manual scrabling, which was added after the scrambling and wouldn't have ever been in the scrambling grid. 

        return 'manual', encrypted_message
    else:
        return 'auto', encrypted_message

def get_manual_decryption_pattern():  #  Prompt user for the manual scrambling pattern. This will be used if detect_shuffle returns 'manual'.
    print()
    encryption_pattern = input("This message was manually encrypted, please paste the shuffle pattern: ").strip()
    print()
    reversed_encryption_pattern = encryption_pattern[::-1]  #  Reverse the order of the  manual scrambling pattern.
    print(f"Reversed Encryption Pattern: {reversed_encryption_pattern}")

    direction_map = {'u': 'D', 'd': 'U', 'l': 'R', 'r': 'L'}  #  Reverse the directions in the reversed scrambling pattern.
    decryption_pattern = ''.join(direction_map[char] for char in reversed_encryption_pattern)  #  Save this as decryption pattern. 
    
    print(f"Decryption Pattern: {decryption_pattern}")
    return decryption_pattern

def message_to_grid(encrypted_message, grid_height, grid_width):
    # Args: encrypted_message (str): The encrypted message to be converted to a grid.
        #   grid_height (int): The height of the grid.
        #   grid_width (int): The width of the grid.
    # Returns: list: A 2D list representing the grid.
    
    grid = []
    start_index = 0
    for i in range(grid_height):
        row = list(encrypted_message[start_index:start_index + grid_width])
        grid.append(row)
        start_index += grid_width

    return grid

def move_blank_space(grid, decryption_pattern):
    # Args: grid (list): A 2D list representing the grid.
      #     decryption_pattern (str): The pattern used for decryption, containing directions (U, D, L, R).
    # Returns: None
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    blank_row, blank_col = find_blank_space(grid)

    for direction in decryption_pattern:
        dr, dc = directions[direction]
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            grid[blank_row][blank_col], grid[new_row][new_col] = grid[new_row][new_col], grid[blank_row][blank_col]
            blank_row, blank_col = new_row, new_col

    return grid

def find_blank_space(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '█':
                return i, j
    return -1, -1

def respaced_words(s):
    #   The undoing of the spaceless_words() function
    s = s.replace('ⓐ', ' A').replace('ⓑ', ' B').replace('ⓒ', ' C').replace('ⓓ', ' D').replace('ⓔ', ' E') \
         .replace('ⓕ', ' F').replace('ⓖ', ' G').replace('ⓗ', ' H').replace('ⓘ', ' I').replace('ⓙ', ' J') \
         .replace('ⓚ', ' K').replace('ⓛ', ' L').replace('ⓜ', ' M').replace('ⓝ', ' N').replace('ⓞ', ' O') \
         .replace('ⓟ', ' P').replace('ⓠ', ' Q').replace('ⓡ', ' R').replace('ⓢ', ' S').replace('ⓣ', ' T') \
         .replace('ⓤ', ' U').replace('ⓥ', ' V').replace('ⓦ', ' W').replace('ⓧ', ' X').replace('ⓨ', ' Y') \
         .replace('ⓩ', ' Z')

    s = s.replace('Ⓐ', 'A').replace('Ⓑ', 'B').replace('Ⓒ', 'C').replace('Ⓓ', 'D').replace('Ⓔ', 'E') \
         .replace('Ⓕ', 'F').replace('Ⓖ', 'G').replace('Ⓗ', 'H').replace('Ⓘ', 'I').replace('Ⓙ', 'J') \
         .replace('Ⓚ', 'K').replace('Ⓛ', 'L').replace('Ⓜ', 'M').replace('Ⓝ', 'N').replace('Ⓞ', 'O') \
         .replace('Ⓟ', 'P').replace('Ⓠ', 'Q').replace('Ⓡ', 'R').replace('Ⓢ', 'S').replace('Ⓣ', 'T') \
         .replace('Ⓤ', 'U').replace('Ⓥ', 'V').replace('Ⓦ', 'W').replace('Ⓧ', 'X').replace('Ⓨ', 'Y') \
         .replace('Ⓩ', 'Z')

    s = s.replace('🄰', ' a').replace('🄱', ' b').replace('🄲', ' c').replace('🄳', ' d').replace('🄴', ' e') \
         .replace('🄵', ' f').replace('🄶', ' g').replace('🄷', ' h').replace('🄸', ' i').replace('🄹', ' j') \
         .replace('🄺', ' k').replace('🄻', ' l').replace('🄼', ' m').replace('🄽', ' n').replace('🄾', ' o') \
         .replace('🄿', ' p').replace('🅀', ' q').replace('🅁', ' r').replace('🅂', ' s').replace('🅃', ' t') \
         .replace('🅄', ' u').replace('🅅', ' v').replace('🅆', ' w').replace('🅇', ' x').replace('🅈', ' y') \
         .replace('🅉', ' z')

    s = s.replace('①', ' 1').replace('②', ' 2').replace('③', ' 3').replace('④', ' 4').replace('⑤', ' 5') \
         .replace('⑥', ' 6').replace('⑦', ' 7').replace('⑧', ' 8').replace('⑨', ' 9').replace('⓪', ' 0')

    s = s.replace('🅐', ' !').replace('🅑', ' "').replace('🅒', ' £').replace('🅓', ' $').replace('🅔', ' %') \
         .replace('🅕', ' ^').replace('🅖', ' &').replace('🅗', ' *').replace('🅘', ' (').replace('🅙', ' )') \
         .replace('¤', ' \\').replace('¶', ' /').replace('§', ' ;').replace('¦', ' :').replace('†', " '") \
         .replace('‡', ' @').replace('•', ' #').replace('◊', ' ~').replace('‹', ' [').replace('›', ' {') \
         .replace('‼', ' ]').replace('‽', ' }').replace('ƒ', ' -').replace('«', ' _').replace('…', ' =') \
         .replace('¿', ' +').replace('×', ' *')

    s = s.replace('ј', '  ').replace('с', '\n')  
    

    return s


def initiate_decryption():
    # Decryption program execution
    global grid_height, grid_width, GridHeight, GridLength, elements
    encrypted_message = collect_encryption()  # Get the encrypted message
    grid_height, grid_width, encrypted_message = define_grid(encrypted_message)
    shuffle_type, encrypted_message = detect_shuffle(encrypted_message)

    if shuffle_type == 'manual': # pass result of get_manual_decryption_pattern() to move_blank_space()
        decryption_pattern = get_manual_decryption_pattern()
        grid = message_to_grid(encrypted_message, grid_height, grid_width)
        grid = move_blank_space(grid, decryption_pattern)
    else:
        elements = "0" * (len(encrypted_message)-1)
        
        GridHeight = grid_height
        GridLength = grid_width
        move_sequence = autoslide(elements)
        # Note that we've passed a 'known grid' of 0s to the existing encryption logic.
        # This known grid has the same dimensions as the grid used to encrypt the input message. 
        # This calculates the the shuffle pattern that would have been used to encrypt the message.

        # Now we reverse the encryption pattern...
        reverse_moves = move_sequence[::-1] 
        decryption_pattern = (
        reverse_moves.replace('U', 'X')
                     .replace('D', 'U')
                     .replace('X', 'D')
                     .replace('L', 'Y')
                     .replace('R', 'L')
                     .replace('Y', 'R'))
        
        # ...and pass it to move_blank_space() function. 
        grid = message_to_grid(encrypted_message, grid_height, grid_width)
        grid = move_blank_space(grid, decryption_pattern)

    # Reading the lines of the unscrambled grid into one string.
    grid_string = "".join("".join(row) for row in grid)  # Join rows
    grid_string = grid_string.replace('█', '')  # Remove '█'
    grid_string = respaced_words(grid_string)
    print()
    print()
    if 'һ' in grid_string:
    # Remove the 'һ' character used to fill the grid for an input with a prime amount of characters. 
        grid_string = grid_string.replace('һ', '')
    print()
    print("decrypted_message: ")
    print()
    print(wrap_text_to_terminal_width(grid_string))       


#============END OF DECRYPTION CODE DEFINITIONS==============


#============MAIN EXECUTION BLOCK============
        
if choice == 'E':
    slidingchoice()
elif choice == 'D':
    # DECYPTION FUNCTION
    initiate_decryption()
elif choice == 'R':
    print ()
    print (wrap_text_to_terminal_width(Read_me1))
    print ()
    input("=======[Press Enter to continue]=======")
    print ()
    print (wrap_text_to_terminal_width(Read_me2))
    print ()
    input("=======[Press Enter to continue]=======")
    print ()
    print (wrap_text_to_terminal_width(Read_me3))
    print ()
 
    choiceR = input("Do you wish to (E)ncrypt a message or (D)ecrypt a JTMS code? ").strip().upper()
    if choiceR == 'E':
        slidingchoice()
    elif choiceR == 'D':
        # DECYPTION FUNCTION
        intinitiate_decryption()
    else:
        print("Invalid choice. Please select either E or D.")

#============RESETTING VARIABLES AND INITIATE TERMINABLE LOOP============
        
choice = ""      
choiceR = ""
choice2 = ""
GridHeight = 0
GridLength = 0

while choice != "F":
    print()
    choice = input("To (F)inish press F, or (E)ncrypt or (D)ecrypt another JTMS code: ").strip().upper()
    
    if choice == 'E':
        slidingchoice()
    elif choice == 'D':
        # DECRYPTION FUNCTION
        initiate_decryption()
    elif choice == 'R':
        print(Read_me)
        input("=======[Press Enter to continue]=======")
        print(Read_me2)
        input("=======[Press Enter to continue]=======")
        print(Read_me3)
     
        choiceR = input("Do you wish to (E)ncrypt a message or (D)ecrypt a JTMS code? ").strip().upper()
        if choiceR == 'E':
            slidingchoice()
        elif choiceR == 'D':
            # DECRYPTION FUNCTION
            initiate_decryption()
        else:
            print("Invalid choice. Please select either E or D.")

print()
print(wrap_text_to_terminal_width("Until we crypt again, cheerio! May your path be lined with success and your days filled with joy."))

    


 
 
