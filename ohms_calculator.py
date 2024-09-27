#add a method to ask the user what to calculate
def ohms_calculator():
    #for asking the user for input if invalid it will ask again
    while True:
        print("What to calculate?\n1. for Voltage (V)\n2. for Current  (I)\n3. Resistance (R)")
        choice = int(input("\nInput 1,2 or 3: "))
        #for getting user choice
        if choice in [1,2,3]:
            break
        #for invalid input
        else:
            print("\nInvalid. Please input 1,2 or 3\n")
        
    if choice == 1:
        current = float(input("\nEnter the current value: "))
        resistance = float(input("\nEnter the resistance value: "))
        voltage = current * resistance
        print(f"The calculated voltage is: {voltage} volts.")
    
    elif choice == 2:
        voltage = float(input("\nEnter the voltage value: "))
        resistance = float(input("\nEnter the resistance value: "))
        if resistance == 0:
            print("\nInvalid. Resistance cannot be zero for this calculation")
        else:
            current = voltage/resistance
            print(f"The current is {current} amperes")
    
    elif choice == 3:
        voltage = float(input("\nEnter the voltage value: "))
        current = float(input("\nEnter the current value: "))
        if current == 0:
            print("\nInvalid. current cannot be zero for this calculation")
        else:
            resistance = voltage/current
            print(f"The current is {resistance} ohms.")


ohms_calculator()

