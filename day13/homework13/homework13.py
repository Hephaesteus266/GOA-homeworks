""" #1 """

i = 1

while i <= 10:
    print(i)
    i += 1

""" #2 """

for num in range(1, 10 + 1):
    if num % 2 == 0:
        print(num)

""" #3 """

numb = int(input("please enter your chosen number: "))

if numb >= 1:
    print("your chosen number is positive!")
elif numb == 0:
    print("your chosen number is Zero!")
else:
    print("your chosen number is a negative!")

""" #4 """

# Main program loop
while True:
    # Ask the user to enter a password
    password = input("Please enter your password: ")

    # Validate the password
    if password == "abc123":
        print("Access granted")
        break
    else:
        print("Access denied. Please try again.")

""" #5 """

num_b = 1

while num_b <= 10:
    print(num_b)
    if num_b == 5:
        break
    num_b += 1

""" #6 """

# Loop until the user enters a valid input
while True:
    # Ask the user to enter a number
    number = int(input("Please enter a number between 1 and 5: "))

    # Check if the number is valid
    if number < 1 or number > 5:
        print("Invalid input. Please try again.")
    else:
        print("Valid input")
        break

""" #7 """

inp_numb = int(input("please enter your chosen number: "))

if inp_numb % 3 == 0:
    print("Fizz")
elif inp_numb % 5 == 0:
    print("Buzz")
elif inp_numb % 3 and inp_numb % 5:
    print("FizzBuzz")
else:
    print(inp_numb)

