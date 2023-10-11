# Import the random module
import random
# CTS 285
# Dataman
# Kent Jones
# 9/25/2023

# Defining addition
def addition():
  print('ADDITION')
  # Declaring Variables
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  sum = num1 + num2
  wrongGuess = 0 # Tracks user guesses
  appRepeat = True # While loop key
  
  # Check if the guess is correct
  while appRepeat == True: 
    print(num1, ' + ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if guess == sum:
      print('C O R R E C T')
      appRepeat = False
    else:
      print('E E E E')
      wrongGuess += 1
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', sum)
        appRepeat = False
     
  # Prompt the user if they would like to repeat the program
  print("1. RETRY\n2. MAIN MENU")
  user_input = int(input("> "))
  if user_input == 1:
    addition()
  elif user_input == 2:
    main()
  else:
      print("ENTER VALID OPTION! LEAVING APPLICATION...")
      main()  
      
# Defining Subtraction
def subtraction():
  print('SUBTRACTION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  difference = num1 - num2
  wrongGuess = 0 # Tracks user guesses
  appRepeat = True # While loop key
  
  # Check if the guess is correct
  while appRepeat == True: 
    print(num1, ' - ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if guess == difference:
      print('C O R R E C T')
      appRepeat = False
    else:
      print('E E E E')
      wrongGuess += 1
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', difference)
        appRepeat = False
        
  # Prompt the user if they would like to repeat the program
  print("1. RETRY\n2. MAIN MENU")
  user_input = int(input("> "))
  if user_input == 1:
    subtraction()
  elif user_input == 2:
    main()
  else:
      print("ENTER VALID OPTION! LEAVING APPLICATION...")
      main()  

# Defining Multiplication
def multiplication():
  print('MULTIPLICATION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  product = num1 * num2
  wrongGuess = 0 # Tracks user guesses
  appRepeat = True # While loop key
  
  # Check if the guess is correct
  while appRepeat == True: 
    print(num1, ' * ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if guess == product:
      print('C O R R E C T')
      appRepeat = False
    else:
      print('E E E E')
      wrongGuess += 1
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', product)
        appRepeat = False
  print("1. RETRY\n2. MAIN MENU")
  user_input = int(input("> "))
  if user_input == 1:
    multiplication()
  elif user_input == 2:
    main()
  else:
      print("ENTER VALID OPTION! LEAVING APPLICATION...")
      main()    
    
# Defining Division
def division():
  print('DIVISION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  quotiant = float(str(round(num1 / num2, 2))) # Rounding quotiant to 2 decimal places

  wrongGuess = 0 # Tracks user guesses
  appRepeat = True # While loop key
  
  # Check if the guess is correct
  while appRepeat == True: 
    print(num1, ' / ', num2, ' = ', '?')
    guess = float(input('What is the answer?: '))
    if guess == quotiant:
      print('C O R R E C T')
      appRepeat = False
    else:
      print('E E E E')
      wrongGuess += 1
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', quotiant)
        appRepeat = False
        
  # Prompt the user if they would like to repeat the program
  print("1. RETRY\n2. MAIN MENU")
  user_input = int(input("> "))
  if user_input == 1:
    division()
  elif user_input == 2:
    main()
  else:
      print("ENTER VALID OPTION! LEAVING APPLICATION...")
      main()  
  
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
    if userInput == 2:
      subtraction()
      repeat = True
    if userInput == 3:
      multiplication()
      repeat = True
    if userInput == 4:
      division()
      repeat = True
    if userInput == 5:
      print('Exiting Program...')
      exit(0)
    else:
      print('INVALID INPUT!')
      
# Calling Main
main()