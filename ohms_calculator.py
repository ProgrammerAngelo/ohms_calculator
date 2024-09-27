#add a method to ask the user what to calculate
def ohms_calculator():
    #for asking the user for input if invalid it will ask again
    while True:
        print("What to calculate?\nInput 1. for Voltage (V)\nInput 2. for Current  (I)\nInput 3. Resistance (R)")
        choice = int(input("Input 1,2 or 3: "))
        #for getting user choice
        if choice in [1,2,3]:
            break
        #for invalid input
        else:
            print("Invalid. Please input 1,2 or 3")

ohms_calculator()

