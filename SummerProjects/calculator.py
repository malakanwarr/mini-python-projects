def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y

while True:
    print("Welcome to Calculator")
    print("What operation would you like to do from the following:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("q for quitting")
    choice = input("Enter your choice: ")
    if choice == "q":
        break
    x= float(input("Enter the first number: "))
    y= float(input("Enter the second number: "))
    if choice == "+":
        print("Result: " + str(add(x, y)))
    elif choice == "-":
        print("Result: " + str(subtract(x, y)))
    elif choice == "*":
        print("Result: " + str(multiply(x, y)))
    elif choice == "/":
        print("Result: " + str(divide(x, y)))
    else:
        print("Invalid choice")







