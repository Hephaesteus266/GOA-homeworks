# for i in range (1, 101): 
#     if i % 2 == 0:
#         label = "Even"
# else:
#     label = "Odd"
# print(str(i) +" is " + label)

for i in range(1, 101):
    label = "even" if i % 2 == 0 else "odd"
    print(f"{i} {label}")

"""ill have to fix this something is wrong"""