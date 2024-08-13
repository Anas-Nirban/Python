logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#caculator operations

#add
def add(n1, n2):
  return n1+n2

#subtract
def subtract(n1, n2):
  return n1-n2

#multiply
def multiply(n1, n2):
  return n1*n2

#divide
def divide(n1, n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))
  for operation in operations:
    print(operation)
  
  should_continue = True
  
  while(should_continue):
    operation_todo = input("Pick an operation from the line above: ")
    num2 = float(input("What is the next number? "))
    calculation_function = operations[operation_todo]
    answer = calculation_function(num1, num2)
  
    print(f"{num1} {operation_todo} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator();

calculator()
