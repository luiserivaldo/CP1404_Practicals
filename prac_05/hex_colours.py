HEX_COLOURS = {"BLACK": "#000000", "DARKGREEN": "#006400", "GRAY": "#bebebe", "HOTPINK": "#ff69b4",
               "LAVENDER": "#e6e6fa", "NAVYBLUE": "#000080", "ORCHID": "#da70d6", "PINK": "#ffc0cb",
               "PURPLE": "#a020f0", "WHITE": "#ffffff"}

colour_input = str(input("Enter colour name: ")).upper()
while colour_input != "":
    if colour_input in HEX_COLOURS:
        print(colour_input, "is", HEX_COLOURS[colour_input])
    else:
        print("Invalid colour")
    colour_input = str(input("Enter colour name: ")).upper()
