print("Luka".replace("L", "k")) #as shown replace function/can only be used with strings

word = "lukatskhvaradze5"

print(word.replace("a", "d")) #HAH
print(word.replace("5", "d")) #hehehehe

def my_replace(word, replace_char, input_char):
    changed_word = ''

    for char in word:
        if char == replace_char:
            changed_word = changed_word + input_char
        else:
            changed_word = changed_word + char
    return changed_word

print(my_replace("lukak", "a", "d"))

print("luka".count("a")) #returns the number of time the given is in the string

print([1,2,2,2,3,4].count(2))

def my_count(collection, count_element):
    count= 0

    for element in collection:
        if element == count_element:
            count = count +1
        
    return count

print(my_count([1,2,2,2,2,3,4], 2))
print("luuuuka".count("u"))

print("fewe".find("we"))
print([1,2,3,4,5].index(4))

def my_find(collection, value):
    for index in range(len(collection)):
        if collection[index] == value:
            return index
    return -1

print(my_find([1,2,3,4,5], 3))
print(my_find([1,2,3,4,5], 8))

def lol_count(array):
    origin = 0
    
    for i in array:
        if i % 2 == 0:
            origin += 1
    return origin

print(lol_count([1,2,3,4,5,6,7,8,9,10]))


def replace_even_indices(input_string, replacement_char):
    result = ""
    for i in range(len(input_string)):
        if i % 2 == 0:  # Check if index is even
            result += replacement_char  # Replace with the specified character
        else:
            result += input_string[i]  # Keep the original character
    return result

print(replace_even_indices("ghostiewordie", "R"))



def find_last_even_index(numbers):
    last_even_index = -1
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            last_even_index = i
    return last_even_index


def find_last_even(numbers_list):
    for i in range(len(numbers_list) -1, -1, -1):
        if numbers_list[i] % 2 == 0:
            return numbers_list[i]
        

print(find_last_even_index([1,2,3,4,5,6,7,8,9,10]))
print(find_last_even([1,2,3,4,5,6,7,8,9,10]))


print("+".join(["1", "2", "3"]))

def my_join(join_str, strings_list):
    joined_elements = ''
    for word in strings_list:
        joined_elements += join_str + word

    return joined_elements[1:]

print(my_join("+", ["1", "2", "3"]))


def process_list(numbers):
    even_numbers = []
    for num in numbers:
        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(str(num))
        return "+".join(even_numbers)
    
    
print(process_list([1,2,3,4,5,6,7,8,9,10]))