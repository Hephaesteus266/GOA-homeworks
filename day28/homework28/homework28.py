def solution(A1, A2):
    if len(A1) < len(A2):
        return False
    elif A1[-len(A2):] == A2:
        return True
    else:
        return False


def solution(text, ending):
    return text.endswith(ending)

def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False

def number(bus_stops):
    num_on_bus = 0

    
    for on, off in bus_stops:      
        num_on_bus += on
        num_on_bus -= off
        
    return num_on_bus

def reverse_words(text):
    words = text.split(' ')
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def arithmetic(a, b, op):
    if op == "add":
        return a +b
    elif op == "subtract":
        return a - b
    elif op == "multiply":
        return a * b
    elif op == "divide":
        return a / b
    else:
        return "invalid Operator"

def solution(identifier):
    words=[]
    word = ""
    for c in identifier:
        if c.isupper():
            """isupper() is a built-in method used to check if a character is an uppercase letter. 
            It returns True if the character is an uppercase letter and False otherwise.

            In the context of the camel casing solution, 
            isupper() is used to identify the uppercase letters in a string, 
            which indicate the beginning of a new word in camel casing. 
            By adding a space before each uppercase letter, 
            the camel case string can be converted to a string with separate words."""
            if word:
                words.append(word)
                word = ""
            word += " "
        word += c
    if word:
        words.append(word)
        return "".join(words)
    

def is_prime(n):
    if n <= 1:
        return False
    if n ==2 or n == 3:
        return True
    if n % 2 ==0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def pyramid(n):
    if n < 0:
        return "n must be non-negative"
    if n == 0:
        return []
    result = []
    for i in range(n):
        row = [1] * (i +1)
        result.append(now)
    return result
