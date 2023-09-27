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
  repeat = False # While loop key
  
  # Check if the guess is correct
  while repeat == False: 
    print(num1, ' + ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', sum)
        repeat = True
    if guess == sum:
      print('C O R R E C T')
      repeat = True
    else:
      print('E E E E')
      wrongGuess += 1
      
# Defining Subtraction
def subtraction():
  print('SUBTRACTION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  difference = num1 - num2
  wrongGuess = 0 # Tracks user guesses
  repeat = False # While loop key
  
  # Check if the guess is correct
  while repeat == False: 
    print(num1, ' - ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', difference)
        repeat = True
    if guess == difference:
      print('C O R R E C T')
      repeat = True
    else:
      print('E E E E')
      wrongGuess += 1

# Defining Multiplication
def multiplication():
  print('MULTIPLICATION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  product = num1 * num2
  wrongGuess = 0 # Tracks user guesses
  repeat = False # While loop key
  
  # Check if the guess is correct
  while repeat == False: 
    print(num1, ' * ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', product)
        repeat = True
    if guess == product:
      print('C O R R E C T')
      repeat = True
    else:
      print('E E E E')
      wrongGuess += 1

# Defining Division
def division():
  print('DIVISION')
  num1 = random.randint(0, 9) # Num ranged between 0 and 20
  num2 = random.randint(0, 9) # Num ranged between 0 and 20
  quotiant = num1 / num2
  wrongGuess = 0 # Tracks user guesses
  repeat = False # While loop key
  
  # Check if the guess is correct
  while repeat == False: 
    print(num1, ' / ', num2, ' = ', '?')
    guess = int(input('What is the answer?: '))
    if wrongGuess == 3: # After third strike, display answer
        print('The Correct answer is ', quotiant)
        repeat = True
    if guess == quotiant:
      print('C O R R E C T')
      repeat = True
    else:
      print('E E E E')
      wrongGuess += 1

def exit_program():
  print("Exiting the program...")
  
# Main Menu
def main():
  repeat = False  # While loop key
  while repeat == False:
    print('WELCOME TO DATAMAN!')
    print('WHAT MATHEMATICAL APPLICATIION WOULD YOU LIKE TO RUN?')
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
      exit_program()
    else:
      print('INVALID INPUT!')
      
# Calling Main
main()