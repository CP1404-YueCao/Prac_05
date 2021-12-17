COLOUR_CODES = {"Aqua": "00ffff", "Aquamarine1": "7fffd4",
                "Aquamarine2": "76eec6", "Aquamarine4": "458b74",
                "Armygreen": "4b5320", "Arylideyellow": "e9d66b",
                "Ashgrey": "b2beb5", "Asparagus": "87a96b",
                "Aureolin": "fdee00", "Azure1": "f0ffff"}
colour_name = input("Please enter a colour name: ")
while 1:
    if colour_name in COLOUR_CODES:
        print(f"The code for {colour_name} is {COLOUR_CODES[colour_name]}.")
    elif colour_name == "":
        break
    else:
        print("Invalid input")
    colour_name = input("Please enter a colour name: ")


