COLOUR_CODES = {"Absolute Zero": "##0048ba", "Acid Green": "#b0bf1a",
                "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00",
                "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                "Apricot": "#fbceb1", "Aqua": "#00ffff"}


colour = input("Enter a colour name: ")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour, please enter another colour")
    colour = input("Enter a colour name: ")
