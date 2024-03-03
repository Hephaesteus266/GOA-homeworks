# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print numbers from the first to the second number
for num in range(num1, num2 + 1 ):
    print(num)


# Get two numbers from the user
numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

# Calculate the sum of numbers in the range
sum = 0
for numb in range(numb1, numb2 + 1):
    sum += numb

# Print the sum
print("The sum of numbers from", numb1, "to", numb2, "is:", sum)

# Print the squares of numbers from 1 to 10
for number in range(1, 11):
    square = number ** 2
    print(square)