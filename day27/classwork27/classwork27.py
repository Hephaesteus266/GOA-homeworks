def minimum(arr):
    min_value = arr[0]
    for i in arr:
        if i < min_value:
            min_value = i
    return min_value

def maximum(arr):
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value

def greet(name):
    greeting = "Hello, "
    greeting1 = " how are you doing today?"
    return greeting + name + greeting1

def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    arr = []
    for i in birds:
        if i not in geese:
            arr.append(i)
    return arr

def find_difference(a, b):
    volume_a = a[0] * a[1] * a[2]
    volume_b = b[0] * b[1] * b[2]
    if volume_a > volume_b:
        difference = volume_a - volume_b
    elif volume_b > volume_a:
        difference = volume_b - volume_a
    return difference

print(find_difference([5,6,7], [7,8,9]))

def is_palindrome(s):
    s = s.lower()
    s_reversed = s[::-1]
    return s == s_reversed

def smash(words):
    return " ".join(words)

def longest(a1, a2):
    s = a1 + a2
    s = set(s)
    s = sorted(s)
    return ''.join(s) 
#i couldn't think of anything else, 
#i used set to basically get rid of duplicates, 
#then sorted for alphabetical order and then join

def cannons_ready(gunners):
    
    for i in gunners:

        if gunners[i] != 'aye':
            return 'Shiver me timbers!'

    return 'Fire!'
    
def sum_two_lowest_numbers(numbers):
    numbers.sort() #this will order the numbers lowest-->highest
    return numbers[0] + numbers[1]

def friend(x):
    friend_list = []
    for i in x:
        if len(i) == 4:
            friend_list.append(i)
    return friend_list

def find_shortest(s):
    words_list = s.split(" ")
    min_length == len(words_list[0])

    for word in words_list:
        if min_length > len(word):
            min_length = len(word)
    return min_length

def find_short(s):
    words_list = s.split(" ")

    len_list = []
    for word in words_list:
        len_list.append(len(word))

    return min(len_list)

def get_middle(s):
    word_length = len(s)
    middle_index = word_length // 2
    
    if word_length % 2 == 1: #if odd
        return s[middle_index]
    else:
        return s[middle_index - 1:middle_index + 1] #if even
    
def high_and_low(numbers):
    numbers = numbers.split()
    highest = int(numbers[0])
    lowest = int(numbers[0])

    for num in numbers:
        if int(num) > highest:
            highest = int(num)
        elif int(num) < lowest:
            lowest = int(num)
            
    highest = str(highest)
    lowest = str(lowest)

    return (highest + " " + lowest)

def highest_and_lowesr(numbers):
    strings_list = numbers.split(" ")
    numbers_list = []
    for number in strings_list:
        numbers_list.append(int(number))
    
    return str(max(numbers_list)) + " " + str(min(numbers_list))

def cannons_ready(gunners):
    
    for i in gunners:

        if gunners[i] != 'aye':
            return 'Shiver me timbers!'

    return 'Fire!'
