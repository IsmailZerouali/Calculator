from art import logo

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mult,
  "/" : div
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for operation in operations:
    print(operation)
  
  switch = False
  while not switch :
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number: "))
    calcul_function = operations[operation_symbol]
    answer = calcul_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    yes_no = input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation.: ")
    if yes_no == "n":
      switch = True
      calculator()
    elif yes_no == "y":
      num1 = answer
calculator()
