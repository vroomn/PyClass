# Useful datatypes
class dualInputs:
    def __init__(self) -> None:
        self.inputOne = None
        self.inputTwo = None

    def gatherInputs(self):
        self.inputOne = input("Parameter one: ")
        self.inputTwo = input("Parameter two: ")

# Intro sequence
print(""""Welcome to the god awful calculator!
All operations are availible under \"help\"""")

# Primary execution process
execute = True
while True:
    # Baseline command
    usrCommand = input("-> ")
    
    match usrCommand.lower():
        #Handle Addition situation
        case "addition":
            usrInput = dualInputs()
            usrInput.gatherInputs()
            result = int(usrInput.inputOne) + int(usrInput.inputTwo)
            print(f"The result is: {result}")
            break
        
        # Command to exit the program
        case "exit":
            execute = False
            break