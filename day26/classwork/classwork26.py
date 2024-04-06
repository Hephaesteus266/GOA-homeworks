start = 0
end = 5
step = 1
while start < end:
    print(start)
    start = start + step


def my_range(start, end, step):
    numbers =[]
    
    while start < end:
        numbers.append(start)
        start = start + step

    return numbers

print(my_range(0,11,1))


numbers = []

for i in range(10 , 50 +1):
    numbers.append(i)


def func(numbers):
    for index in range(len(numbers) -1, -1, -1):
        if numbers[index] % 4 ==0:
            return numbers[index]
        
print(func(numbers))


def custom_range(start, stop, step=1):
    array = []
    num = start
    while num < stop:
        array.append(num)
        num += step

    return array

print(custom_range(1, 10 ,2))


def filter(collection, variable):
    result = []
    for i in collection:
        if i != variable:
            result.append(i)
    return ''.join(result)

print(filter("abcdd", "d"))

def hypothenuse(leg1, leg2):
    return (leg1**2 + leg2**2)**0.5
print(hypothenuse(5,9))



def capitalization(user):
    
    if len(user) <+ 5:
        return user.capitalize()
    if len(user) > 5:
        return user.upper()
    

user = input("Enter your name:")
print(capitalization(user))