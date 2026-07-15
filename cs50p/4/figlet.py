from pyfiglet import Figlet
import random
import sys

def main():
    # Initialize the figlet object
    figlet = Figlet()
    # Fetch all available fonts into a list
    available_fonts = figlet.getFonts()

    # Case 1: No arguments provided (Random Font)
    if len(sys.argv) == 1:
        font_choice = random.choice(available_fonts)
        
    # Case 2: Specific font requested (Two extra arguments)
    elif len(sys.argv) == 3:
        # Fixed logic: must not be -f AND must not be --font to fail
        if sys.argv[1] != '-f' and sys.argv[1] != '--font':
            sys.exit("Invalid usage")
            
        # Check if the requested font actually exists
        if sys.argv[2] not in available_fonts:
            sys.exit("Invalid font name")
            
        font_choice = sys.argv[2]
        
    # Case 3: Any other number of arguments is invalid
    else:
        sys.exit("Invalid usage")

    # Prompt user for text after validating arguments
    text_input = input("Input: ")
    
    # Set font and output the ASCII art
    figlet.setFont(font=font_choice)
    print(f"Output:\n{figlet.renderText(text_input)}")

if __name__ == "__main__":
    main()
