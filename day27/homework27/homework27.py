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