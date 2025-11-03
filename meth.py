import time
from calculator import add, subtract, multiply, divide

print("welcome to the most basic calculator ever, i hope you hate it here as much as i do")
time.sleep(1)

def calculator():
    print("screw you for even trying to use this")
    time.sleep(1)
    print("just a regular calculator, options; + for add, - for subtract, * for multiply, / for divide")
    time.sleep(1)

    operation = input("what operation do you want").strip()
    time.sleep(2)

    try:
        num1 = float(input("first number, if you absolutely have to: "))
        time.sleep(1)
        num2 = float(input("second number, hooray: "))
        time.sleep(1)
    except ValueError:
        print("are we joking right now? you should know that isnt a number")
        return

    if operation == '+':
        print("amazing, basic addition:", add(num1, num2))
    elif operation == '-':
        print("fantastic, basic subtraction:", subtract(num1, num2))
    elif operation == '*':
        print("wow, basic multiplication:", multiply(num1, num2))
    elif operation == '/':
        result = divide(num1, num2)
        if result is not None:
            print("incredible, basic division:", result)
    else:
        print("i literally hate my life. this is not even an option.")
    
calculator()