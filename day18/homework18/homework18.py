def filter_multiples_of_four(numbers):
    new_list = []
    for num in numbers:
        if num % 4 == 0:
            new_list.append(num)
    return new_list

def add_names_to_list(first_name, last_name):
    names = []
    names.append(first_name)
    names.append(last_name)
    return names

def get_numbers_between(start, end):
    numbers = []
    for i in range(start, end + 1):
        numbers.append(i)
    return numbers

def filter_even_indices(numbers):
    new_list = []
    for i in range(len(numbers)):
        if i % 2 != 0:
            new_list.append(numbers[i] ** 0.5)
        else:
            new_list.append(numbers[i] ** 2)
    return new_list

def reverse_word(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

def remove_duplicates(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

def get_arithmetic_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

#============
# def filter_arr(start_num, end_num):
#     numbers= []
#     filtered_list =[]

#     for i in range(start_num, end_num):
#         numbers.append(1)

#     print(numbers)
    
#     for i in numbers:
#         if i % 2 == 0:
#             filtered_list.append(i ** 2)
#         else:
#             filtered_list.append(i ** 0.5)
    
#     return filtered_list



# start_num = int(input("Please enter first number: "))
# end_num = int(input("Please enter second number: "))

# result_list = filter_arr(start_num,end_num)

# print(result_list)

# #==============2

# def filter_list(start_num, end_num):
#     filtered_list = []
#     for i in range(start_num,end_num):
#         if i % 2 == 0:
#             filtered_list.append(i ** 2)
#         else:
#             filtered_list.append(i ** 0.5)
    
#     return filtered_list



# start_num = int(input("Please enter first number: "))
# end_num = int(input("Please enter second number: "))

# result_list = filter_list(start_num,end_num)

# print(result_list)
#==================1


# def even_indexes(lastname):
#     char_list=[]
#     even_index_chars = []

#     for char in lastname:
#         char_list.append(char)

#     for index in range(len(char_list)):
#         if index % 2 == 0:
#             even_index_chars.append(char_list[index])

#     return(even_index_chars)



# lastname = input("please enter lastname: ")

# print(even_indexes(lastname))

#===============2

# def even_indexes(lastname):
#     even_index_chars = []

#     for index in range(len(lastname)):
#         if index % 2 ==0:
#             even_index_chars.append(lastname[index])

#     return(even_index_chars)


# lastname = input("please enter lastname: ")

# print(even_indexes(lastname))

#===============bonus1

# def even_indexes(lastname):
#     even_index_chars = []

#     for index in range(len(lastname)):
#         if index % 2 ==0:
#             even_index_chars.append(lastname[index])

#     return ''.join(even_index_chars)


# lastname = input("please enter lastname: ")

# print(even_indexes(lastname))

#================bonus2
# def even_indexes(lastname):
#     result = ''

#     for index in range(len(lastname)):
#         if index % 2 ==0:
#             result = result + lastname[index]

#     return(result)


# lastname = input("please enter lastname: ")

# print(even_indexes(lastname))


