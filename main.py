#Define four subroutines - add, subtract, multiply, divide that add multiply etc two numbers and return the result. Each should have two integer number arguments.
#The user is asked to input two numbers.  These numbers will be passed as arguments into one of the subroutines.

def add(num1, num2):
  return num1 + num2
  

def subtract(num1, num2):
  return num1 - num2
  

def multiply(num1, num2):
  return num1 * num2


def divide(num1, num2):
  return num1 / num2




#The user is asked to input 1 to add, 2 to subtract etc.
#If they input 1, call the ‘add’ subroutine, input 2 calls the ‘subtract’ subroutine etc
#Output the returned result as part of a sentence.

calculator = int(input("Input 1 to add: Input 2 to subtract: Input 3 to multiply: Input 4 to divide"))

if calculator == 1:
  numb1 = int(input("Enter one number to add"))
  numb2 = int(input("Enter another number to add"))
  outputAdd = (add(numb1, numb2))
  print(str(outputAdd) + " is your answer.")

elif calculator == 2:
  numb1 = int(input("Enter one number to subtract"))
  numb2 = int(input("Enter another number to subtract"))
  outputSub = (subtract(numb1, numb2))
  print(str(outputSub) + " is your answer.")
elif calculator == 3:
  numb1 = int(input("Enter one number to multiply"))
  numb2 = int(input("Enter another number to multiply"))
  outputMulti = (multiply(numb1, numb2))
  print(str(outputMulti) + " is your answer.")
elif calculator == 4:
  numb1 = int(input("Enter one number to divide"))
  numb2 = int(input("Enter another number to divide"))
  outputDiv = (divide(numb1, numb2))
  print(str(outputDiv) + " is your answer")
else:
  print("Error: Please enter a valid calculator mode")
