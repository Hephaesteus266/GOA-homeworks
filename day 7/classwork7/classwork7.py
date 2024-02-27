""" data conversion"""
num = 1265

result = 0

str_num = str(num)
for i in str_num:
    result = result + int(i)
print(result)

"""Comparison Operations"""

print(30 < 25)
print (5 < 9)
print (50 > 100)

"""type function"""

Age = 16 
name = "sandro"
player_health = 12.5
alive = 5 > 3

print(type(Age))
print(type(name))
print(type(player_health))
print(type(alive))

# boolean has one of two types of values : True or False


"""logical operations"""
# Logical Operations are executed with the data type 'Boolean' and it's brought forth with print() function

num1 = 10
num2 = 10


# with 'or' in a situation such as True or False, True will always be printed
print (num1 > 5 or num1 < 3)

# with 'and' in a situation such as True and True, True will be printed
print(num1 > 2 and num2 < 12)

# with 'and' in a situation such as True and False, False will be printed
print(num1 < 4 and num2 < 6)

# as in True will prevail no matter what in 'or' situations
# but it will have to yield in the face of False when confronted with 'and'


"""Classwork below"""

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# homework is to do the above but with numbers. also draw a castle with turtle with a queen and king. + solo learn Module 3 quiz