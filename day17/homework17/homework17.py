def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def filter_string(strings):
    filtered_strings = []
    for string in strings:
        if len(string) > 5:
            filtered_strings.append(string)
    return filtered_strings

def filter_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 ==0:
            even_numbers.append(number)
    return even_numbers

def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

def filter_strings_starting_with_a(strings):
    strings_with_a = []
    for string in strings:
        if string[0] == 'a':
            strings_with_a.append(string)
    return strings_with_a

def square_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

def get_lengths(strings):
    lengths = []
    for string in strings:
        lengths.append(len(string))
    return lengths

def sum_numbers_greater_than_10(numbers):
    sum = 0
    for number in numbers:
        if number > 10:
            sum += number
    return sum