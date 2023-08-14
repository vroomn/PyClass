from math import sqrt

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
        
        # Subtraction
        case "subtract":
            addSub(-1)

        # Multiplication
        case "multiply":
            usrInput = dualInputs()
            result = int(usrInput.inputOne) * int(usrInput.inputTwo)
            print(f"The result is: {result}")

        case "divide":
            usrInput = dualInputs()
            result = int(usrInput.inputOne) / int(usrInput.inputTwo)
            print(f"The result is: {result}")

        # Exponential
        case "exponential":
            usrInput = dualInputs()
            result = int(usrInput.inputOne) ** int(usrInput.inputTwo)
            print(f"The result is: {result}")

        # Square Root
        case "square root":
            usrInput = input("Parameter to square root: ")
            result = sqrt(int(usrInput))
            print(f"The result is: {result}")

        # Command to exit the program
        case "exit": break
