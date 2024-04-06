def grow(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
    

def bmi(weight, height):
    bmi_OK= weight / (height ** 2)
    
    if bmi_OK <= 18.5:
        return "Underweight"
    elif bmi_OK <= 25.0:
        return "Normal"
    elif bmi_OK <= 30.0:
        return "Overweight"
    else:
        return "Obese"
    
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

def square_digits(num):
    num_string = str(num)
    result = ""
    
    for i in num_string:
        result += str(int(i) ** 2)
    return int(result)


def descending_order(num):
    res_str = ""
    num_str = str(num)
    reverse_str = ""
    res_arr = []
    
    for i in range(len(num_str)-1, -1, -1):
        reverse_str += num_str[i]
        
    for i in reverse_str:
        res_arr.append(i)
        res_arr.sort(reverse = True)
    return int("".join(res_arr))