# number = int(input("please enter your chosen number: "))

# if number > 0:
#     print("The chosen number is positive!")
# elif number < 0:
#     print("the chosen number is negative!")
# else:
#     print("the chosen number is 0!")
        


# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num)

# numb = int(input("please enter a number: "))
# sum = 0

# while numb > 0:
#     sum += numb
#     numb = int(input("please enter a number (0 to stop): "))
# print("the sum is:", sum)

# # need to work on the while loop more!

# correct_pin = 1234

# pin = int(input("Enter Your correct PIN: "))

# if pin == correct_pin:
#     print("welcome to the ATM!")
#     print("1. withdrawal")
#     print("2. deposit")
#     print("3. Balance")

# corr_password = "password123"
# username = "Admin"

# user_name = input("Please enter your username: ")
# password = input("Please enter your password: ")

# if corr_password == password and username == user_name:
#     print("Login Successful!")
# else:
#     print("login unsuccessful, Try again in a minute!")


age = int(input("Please enter your age: "))

if age < 13:
    print("You are a child")
elif age <= 17:
    print("you are a teenager")
else:
    print("You are an adult")