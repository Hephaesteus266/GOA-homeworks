def century(year):
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1
    
def count_sheeps(sheep):
    if sheep == []:
        return 0
    else:
        count = 0
        for i in sheep:
            if i == True
            count += 1
    return count

def find_smallest_int(arr):
    minimum = arr[0]
    for i in arr:
        if minimum > i:
            minimum = i
    return minimum

def litres(time):
    return (time * 0.5) // 1

def reverse_seq(n):
    new_list = []
    for i in range(n, 0, -1):
        new_list.append(i)
    return new_list

def square_or_square_root(arr):
    new_list = []
    for i in arr:
        if i**0.5 * i**0.5 == i:
            new_list.append(i**0.5)
        else:
            new_list.append(i**2)
    return new_list

def bonus_time(salary, bonus):
    if bonus == True:
        return f"${salary * 10}"
    else:
        return f"${salary}"
    
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False
    
def find_average(numbers):
    if numbers == []:
        return 0
    else:
        sum = 0
        for i in numbers:
            sum += 1
        return sum / len(numbers)
    
def double_char(s):
    new_list = []
    for i in s:
        new_list.append(i *2)
    return "".join(new_list)

def invert(lst):
    new_list = []
    for i in lst:
        i = -i
        new_list.append(i)
    return new_list

def minimum(arr):
    minimum = arr[0]
    for i in arr:
        if minimum > i:
            minimum = i
    return minimum

def maximum(arr):
    maximum = arr[0]
    for i in arr:
        if maximum < i:
            maximum = i
    return maximum

#--------------------------------PART 2

def to_weird_case(words):
    words = words.split(" ")
    res_list = []
    for word in words:
        modi_str = ""

        for i in range(len(word)):
            if i % 2 ==0:
                modi_str += word[i].upper()
            else:
                modi_str += word[i].lower()

    return " ".join(res_list)

def camel_case(str):
    res_list = []
    str = str.split(" ")
    for word in str:
        res_list.append(word.capitalize())
    return "".join(res_list)

def validate_pin(pin): 
    if len(pin) == 4 or len(pin) == 6:
        is_valid = True

        numbers = "0123456789"

        for i in pin:
            if i not in numbers:
                is_valid = False
        return is_valid
    return False


def variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance






