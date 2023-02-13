# Calculator

operation = str(input("Which operation do you want to do? "))

a = int(input("1st number: "))
b = int(input("2nd number: "))

while True:
  if operation == ("+"):
    print(a + b)
  elif operation == ("-"):
    print(a - b)
  elif operation == ("*"):
    print(a * b)
  elif operation == ("/"):
    print(a / b)
  else:
    print("Wrong operation")
  break