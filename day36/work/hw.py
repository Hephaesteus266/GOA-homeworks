def manual_reverse(collection):
    reversed_collection = []
    for i in range(len(collection) - 1, -1, -1):
        reversed_collection.append(collection[i])
    return reversed_collection

def manual_replace(lst, old_element, new_element):
    replaced_collection = []
    for element in lst:
        if element == old_element:
            replaced_collection.append(new_element)
        else:
            replaced_collection.append(element)
    return replaced_collection

def manual_count(collection, value):
    count = 0
    for element in collection:
        if element == value:
            count += 1
    return count

#i hope to the fuvking pantheons these work


def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s == True:
            count += 1
    return count

def find_needle(haystack):
    for i, x in enumerate(haystack):
        if x == "needle":
            return i

def valid_parentheses(parens):
    stack = []
    for p in parens:
        if p == "(":
            stack.append(p)
        elif p == ")":
            if not stack or stack.pop() != "(":
                return False
    return not stack

def find_uniq(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

def digital_root(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

def find_even_index(arr):
    for i, x in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i

def count_bits(n):
    count = 0
    while n > 0:
        if n % 2 == 1:
            count += 1
        n = n // 2
    return count

def square_digits(num):
    num_str = str(num)
    num_list = []
    for digit in num_str:
        num_list.append(int(digit)**2)
    return int("".join(str(x) for x in num_list))

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def count_smileys(arr):
    count = 0
    for face in arr:
        if len(face) == 2 or (len(face) == 3 and face[1] in ["-", "~"]):
            if face[0] == ":" or face[0] == "^":
                if face[1] == ":" or face[1] == "^":
                    count += 1
    return count

def sum_digits(n):
    n_str = str(n)
    n_list = []
    for digit in n_str:
        n_list.append(int(digit))
    return sum(n_list)
