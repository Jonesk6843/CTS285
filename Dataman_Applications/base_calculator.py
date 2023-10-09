# Main Menu
def main():
  repeat = False  # While loop key
  while repeat == False:
    print('WELCOME TO DATAMAN!')
    print('WHAT MATHEMATICAL APPLICATIION WOULD YOU LIKE TO RUN?')
    print('1. ADDITION')
    print('2. SUBTRACTION')
    print('3. MULTIPLICATIION')
    print('4. DIVISION')
    print('5. EXIT')
    userInput = int(input('> '))
    if userInput == 1:
      addition()
      repeat = True
    elif userInput == 2:
      subtraction()
      repeat = True
    elif userInput == 3:
      multiplication()
      repeat = True
    elif userInput == 4:
      division()
      repeat = True
    elif userInput == 5:
      exit()
    else:
      print('INVALID INPUT!')
      
# Applications
def addition():
    repeat = True
    while repeat:
        user_num1 = float(input("ADDITION!\nENTER A NUMBER: "))
        user_num2 = float(input("ADD IT TO: "))
        
        result = addition_calc(user_num1, user_num2)
        
        print(f"{user_num1} + {user_num2} = {result:.1f}")
        
        print("1. RETRY\n2. MAIN MENU")
        user_input = int(input("> "))
        if user_input == 1:
            repeat = True
        elif user_input == 2:
            repeat = False
            main()
        else:
            print("ENTER VALID OPTION! RESETING ADDITION PROGRAM!")
            
def subtraction():
    repeat = True
    while repeat:
        user_num1 = float(input("SUBTRACTION!\nENTER A NUMBER: "))
        user_num2 = float(input("SUBTRACT IT TO: "))
        
        result = subtraction_calc(user_num1, user_num2)
        
        print(f"{user_num1} - {user_num2} = {result:.1f}")
        
        print("1. RETRY\n2. MAIN MENU")
        user_input = int(input("> "))
        if user_input == 1:
            repeat = True
        elif user_input == 2:
            repeat = False
            main()
        else:
            print("ENTER VALID OPTION! RESETING SUBTRACTION PROGRAM!")
            
def multiplication():
    repeat = True
    while repeat:
        user_num1 = float(input("MULTIPLICATION!\nENTER A NUMBER: "))
        user_num2 = float(input("ADD IT TO: "))
        
        result = multiplication_Calc(user_num1, user_num2)
        
        print(f"{user_num1} * {user_num2} = {result:.1f}")
        
        print("1. RETRY\n2. MAIN MENU")
        user_input = int(input("> "))
        if user_input == 1:
            repeat = True
        elif user_input == 2:
            repeat = False
            main()
        else:
            print("ENTER VALID OPTION! RESETING MULTIPLICATION PROGRAM!")

def division():
    repeat = True
    while repeat:
        user_num1 = float(input("DIVISION!\nENTER A NUMBER: "))
        user_num2 = float(input("DIVIDE IT BY: "))
        if user_num2 == 0:
            print("ERROR ERROR! THAT'S NOT POSSIBLE!")
        else:    
            result = division_Calc(user_num1, user_num2)
            print(f"{user_num1} / {user_num2} = {result:.1f}")
        print("1. RETRY\n2. MAIN MENU")
        user_input = int(input("> "))
        if user_input == 1:
            repeat = True
        elif user_input == 2:
            repeat = False
            main()
        else:
            print("ENTER VALID OPTION! RESETING DIVISION PROGRAM!")

# Calculators
def addition_calc(num1, num2):
    sum_value = num1 + num2  # Perform the addition calculation
    return sum_value # Return the sum

def subtraction_calc(num1, num2):
    difference_value = num1 - num2  # Perform the subtraction calculation
    return difference_value # Return the difference

def multiplication_Calc(num1, num2):
    product_value = num1 * num2  # Perform the addition calculation
    return product_value # Return the product

def division_Calc(num1, num2):
    quotiant_value = num1 / num2  # Perform the addition calculation
    return quotiant_value # Return the quotiant

# Calling Main
main()