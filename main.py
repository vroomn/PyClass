# Intro sequence
print(""""Welcome to the god awful calculator!
All operations are availible under \"help\"""")

# Primary execution process
execute = True
while True:
    # Baseline command
    usrCommand = input("-> ")
    
    match usrCommand.lower():
        # Command to exit the program
        case "exit":
            execute = False
            break