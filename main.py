# Useful datatype for two inputs from the user
class dualInputs:
    def __init__(self) -> None:
        self.inputOne = input("Parameter one: ")
        self.inputTwo = input("Parameter two: ")

# Function to reduce reused code
def addSub(modifier):
    usrInput = dualInputs()
    result = int(usrInput.inputOne) + (int(usrInput.inputTwo) * modifier)
    print(f"The result is: {result}")

# Intro sequence
print(""""Welcome to the god awful calculator!
All operations are availible under \"help\"""")

# Primary execution process
while True:
    # Baseline command
    usrCommand = input("-> ")
    
    # Switch statement to choose operation mode
    match usrCommand.lower():
        #Handle Addition situation
        case "add":
            addSub(1)
        
        case "subtract":
            addSub(-1)

        # Command to exit the program
        case "exit": break
    