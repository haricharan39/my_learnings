def hello(input1):
    print(f"Hello, {input1}!")

hello(input("What is your name? "))

def addition(num1 = 0, num2 = 0):
    return int(num1) + int(num2)

result1 = addition(input("Enter a number: "), input("Enter another number: "))
print(f"{result1}")

def subtraction(num1 = 0, num2 = 0):
    return int(num1) - int(num2)

result2 = subtraction(input("Enter a number: "), input("Enter another number: "))
print(f"{result2}")

def multiplication(num1 = 0, num2 = 0):
    return int(num1) * int(num2)

result3 = multiplication(input("Enter a number: "), input("Enter another number: "))
print(f"{result3}")

def division(num1 = 0, num2 = 0):
    if int(num2) == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(int(num1) / int(num2))

division(input("Enter a number: "), input("Enter another number: "))

def square(num1 = 0):
    return int(num1) ** 2

result5 = square(input("Enter a number: "))
print(f"{result5}")
