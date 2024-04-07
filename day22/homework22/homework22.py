def remove_char(s):
    return s[1:-1]
    


def square_sum(numbers):
    total = 0
    for i in numbers:
        total += i**2
    return total

def summation(num):
    total = 0
    for i in range(1, num +1 ):
        total += i
    return total
        
def string_to_number(s):
    s = int(s)
    return s

def number_to_string(num):
    num = str(num)
    return num

def disemvowel(string_):
    vowels = "aieouAIEOU"
    result = []
    for i in string_:
        if i not in vowels:
            result.append(i)
    return "".join(result)


def high_and_low(numbers):
    numbers = numbers.split()
    highest = int(numbers[0])
    lowest = int(numbers[0])

    for num in numbers:
        if int(num) > highest:
            highest = int(num)
        elif int(num) < lowest:
            lowest = int(num)

    return (highest, lowest)

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result