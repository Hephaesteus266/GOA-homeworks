""" #2 """

sum = 0
num = 1 

while num <= 10:
    if num % 2 == 0:
        sum += num
    num += 1
print(sum)




""" #3 """

numb = 1

while numb <= 20:
    if numb % 3 == 0 and numb % 5 == 0:
        print(numb)
    numb += 1




""" #4 """

for i in range(1, 101):
    if i % 5 == 0:
        print(i)
    i += 1




""" #5 """

for div in range(1,21):
    if div % 6 == 0:
        print(div)
    div += 1