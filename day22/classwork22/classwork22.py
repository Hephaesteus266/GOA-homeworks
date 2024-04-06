def grow(arr):
    product = 1
    for num in arr:
        product *= num
    return product

def bmi(weight, height):
    body_mass_index = weight/(height ** 2)
    if body_mass_index <= 18.5:
        return "Underweight"
    elif body_mass_index <= 25.0:
        return "Normal"
    elif body_mass_index <= 30.0:
        return "Overwight"
    else:
        return "Obese"
    
def get_count(sentence):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in sentence:
        if char in vowels:
            count += 1
        return count
    
def square_digits(num):
    num = str(num)
    num = list(num) #list() function creates a list
    
    new_arr = []
    for i in num:
        new_arr.append(int(i))
    
    res_str = ""
    for i in new_arr:
        squared = i ** 2
        res_str += str(squared)
    return int(res_str)

def descending_order(num):
    num = str(num)
    num = list(num)

    new_arr = []
    for x in num:
        new_arr.append(int(x))
    new_arr.sort(reverse = True) # the sort function reverses the flow of numbers whether it be TRUE or FALSE

    res_str = ''
    for i in new_arr:
        res_str += str(i)
    return int(res_str)

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
 
def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:  #length function
        return names[0] + " likes this"
    elif len(names) == 2:
        return names[0] + " and " + names[1] + " like this"
    elif len(names) == 3:
        return names[0] + ", " + names[1] + " and " + names[2]+ "like this"
    else:
        return names[0] + " , " + names[1] + " and " + str(len(names) - 2) + " others like this"



item = "Ghost"
item2 = 'GHOST'
print(item.upper())
print(item.lower())
print(item.capitalize())
print(item2.capitalize()) 
print(item.find("s")) #find the index of the given letter

print(item.find("A")) #if the given letter cant be found, -1 will be returned

sentence = "Hello, world! How are you today?"
words = sentence.split()  # Splitting using whitespace by default
print(words)
# Output: ['Hello,', 'world!', 'How', 'are', 'you', 'today?']

numbers = "1,2,3,4,5"
num_list = numbers.split(",")  # Splitting using comma as separator
print(num_list)
# Output: ['1', '2', '3', '4', '5']

#list functions

movies = ["Avatar", "Titanic", "Avengers"]
print(len(movies)) #len = length which returns the number of items in the list

movie = "Avengers"
print(len(movie)) #it can also return for just strings

songs = ["yesterday", "Hello", "Believer"]
songs.append("Imagine") #adds another string to an already existing list
print(songs)

items = ["book", "pen", "pencil"]
items.insert(2, "marker") #the insert() func adds an element to a list (marker), at a specific position (2)
print(items)
print(items[2])

items.pop(1) #pop() func removes an element from a list via its index
print(items)
print(items[1])

