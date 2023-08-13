# Useful datatypes
class dualInputs:
    def __init__(self) -> None:
        self.inputOne = input("Parameter one: ")
        self.inputTwo = input("Parameter two: ")

# Intro sequence
print(""""Welcome to the god awful calculator!
All operations are availible under \"help\"""")

# Primary execution process
while True:
    # Baseline command
    usrCommand = input("-> ")
    
    match usrCommand.lower():
        #Handle Addition situation
        case "addition":
            usrInput = dualInputs()
            result = int(usrInput.inputOne) + int(usrInput.inputTwo)
            print(f"The result is: {result}")
        
        case "subtract":
            continue

        # Command to exit the program
        case "exit": break
    