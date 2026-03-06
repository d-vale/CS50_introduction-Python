import sys
import random
from pyfiglet import Figlet

# Initialize Figlet and retrieve the list of available fonts
figlet = Figlet()
fonts = figlet.getFonts()

# If no arguments are provided, pick a random font
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))
# If -f or --font flag is provided with a font name, use that font
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font=sys.argv[2])
# Any other argument combination is invalid
else:
    sys.exit("Invalid usage")

# Prompt the user for input and render it in the chosen font
text = input("Input: ")
print(figlet.renderText(text))
