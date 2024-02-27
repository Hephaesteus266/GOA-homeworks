# registered_password = "mariam1234"
# authorized = False

# # pushups = 5

# # if pushups == 10:
# #     print("hello") #true
# # else:
# #     print("") #False


# while authorized != True:
#     user_input = input("Please enter your password")

#     if user_input == registered_password:
#         print("Access Granted")
#         authorized = True
#     else:
#         print("password incorrect")


# guess = "cat"
# word = "dog"
# if guess == word:
#     print("good one")
# else: 
#     print("try again")

# score = 95
# if score > 90:
#     print("great job")
#     print("level complete")
# else:
#     print("Game over")

#user will input a number between 1-1-, ifinput is 5 lets return that he won
#if the inputted number is 9, he lost 
number = int(input("please enter the number between 1-10: "))

if number == 5:
    print("You won")
elif number == 9:
    print("you won half prize")
else:
    print("you lost")
