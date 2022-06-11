# This is a sample Python script for a calculator.
num = float(input("Enter first number: "))
op = input("Enter an operator: ")
num1 = float(input("Enter first number: "))

if op == "+":
    print(num + num1)
elif op == "*":
    print(num * num1)
elif op == "*":
    print(num - num1)
elif op == "-":
    print(num - num1)
elif op == "/":
    print(num/num1)
else:
    print("invalid operator")
