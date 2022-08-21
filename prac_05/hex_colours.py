code_to_colours = {"Absolute Zero" : "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc"}
print(code_to_colours)

code = input("Enter colour name: ")
while code != "":
    if code in code_to_colours:
        print("Code of {} is {}".format(code, code_to_colours[code]))
    else:
        print("Invalid spelling")
    code = input("Enter colour name: ").lower()
