import sys

def add(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2): 
    res = num1 - num2
    return res

def mul(num1, num2):
    res = num1 * num2
    return res

def div(num1, num2):
    res = num1 // num2
    return res


num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    print(add(num1, num2))
elif operation == "sub":
    print(sub(num1, num2))
elif operation == "mul":
    print(mul(num1, num2))
elif operation == "div":
    print(div(num1, num2))
else:
    print("Invalid operation")