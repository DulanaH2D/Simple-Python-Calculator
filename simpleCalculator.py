# Arithmatic operations on two numbers
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("float division by zero")
        return "None"
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Select operation
def select_op(choice, a, b):
    if choice == '+':
        return add(a, b)
    elif choice == '-':
        return subtract(a, b)
    elif choice == '*':
        return multiply(a, b)
    elif choice == '/':
        return divide(a, b)
    elif choice == '^':
        return power(a, b)
    elif choice == '%':
        return remainder(a, b)
    elif choice == '#':
        print("Done. Terminating")
        exit()
    elif choice == '$':
        return None
    else:
        return "Unrecognized operation"
        
# Main 
while True:
    print("Select operation.")
    print("1.Add      : +")
    print("2.Subtract : -")
    print("3.Multiply : *")
    print("4.Divide   : /")
    print("5.Power    : ^")
    print("6.Remainder: %")
    print("7.Terminate: #")
    print("8.Reset    : $")
    
    user_input = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(user_input)
    
    
    if (user_input == "#"):
        print("Done. Terminating")
        break
    elif "$" in user_input:
        continue    
    else:
        fnum = input("Enter first number: ")
        print(fnum)
        if fnum.endswith("$"):
            continue
        if fnum == "#":
            print("Done. Terminating")
            break
            
        snum = input("Enter second number: ")
        print(snum)
        if snum.endswith("$"):
            continue
        if snum == "#":
            print("Done. Terminating")
            break
        
        # calculate the result
        result = select_op(user_input, float(fnum), float(snum))
        if result is not None:
            print(float(fnum), user_input,float(snum), "=", result)
