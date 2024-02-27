# name = "nika"
# print(name)




# print ("your age is: " + age)

# age= age + 10
# print("after ten years you will be: " + age)
# ---------------
# first lets declare the intended variables
"""second since we are using integers we will have to "turn the tables" so to speak
on the input() by using int(input())"""

num1 = int(input("please choose your first number: "))
num2 = int(input("now your second number: "))
num3 = int(input("last but not least, your third number: "))


"""for future references we might need to use the calculated number later on,
so it's better to save it in a variable for future use"""

result = num1*num2*num3
Answer = "the product of your chosen numbers is: "

# now the last step is to execute the commands with the print function!

"""however, since the variable result contains a value that is a product of integers it wont be
printed with a string type, that is why we need to use str() for the variable result so its value
will be brought forth"""

print(Answer + str(result))


# -----------------------------

#first we declare string type variables which contain values such as your name and surname
# we also need to declare the integer type of variable containing the value that is age.
# we will be using input() for string type variables and int(input()) for integers.

name =input("please indicate your name: ")
surname = input("now if you please indicate your surname: ")
age = int(input("and last but not least, please indicate your age: "))

# now to declare a string type of variable (+int) containing the greeting!
greeting_nm_srnm = "Hello i am " + name + " " + surname
greeting_age = " and i am " + str(age) + " years old"

# now to use the print function to bring the commands forth

print(greeting_nm_srnm + greeting_age)



