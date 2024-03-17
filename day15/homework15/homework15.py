num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is not even. The next even number is", num + 1, ".")


count = 0
while True:
    password = input("Enter the password: ")
    count =+ 1
    if password == "Goa best":
        break
print("Incorrect passwords entered:", count)

def starts_with_g(s):
    return s[0] == "G"

names = []
for i in range(5):
    name = input("enter name #" + str(i +1)+ ": ")
    names.append(name)
print("First three names:", names[:3])

def is_prime(n):
    if n <2:
        for i in range(2, n):
            if n %i ==0:
                return False
        return True
    
i = 10
while i >= 0:
    print(i)
    i -= 1

def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if operator == "+":
        result = num1 +num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("error! Divison by zero cannot be done")
            return
        result = num1 / num2
    else: 
        print ("Error: Invalid ")
        return
    print("result", result)

name = input("Enter name: ")
print("last character is: ", name[-1])

num = int(input("enter a number: "))
even_numbers = []
for i in range(num +1):
    if i % 2 == 0:
        even_numbers.append(i)
print("even numbers: ", even_numbers)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n - 1)

num = int(input("Enter a number: "))
print("factorial of", num, ":", factorial(num))