""" LISTS """

#Lists allow you to store multiple values in a single variable

#Although single values are encased in just brackets ( )
#to store multiple values we need to encase them in square brackets [ ]
#and end each of them with a comma, except for last. Just like a list!




animals = ["cat", "dog", "bird"]

#P.S. values still need to be encased in " " if they are strings 
#also without the comma it basically makes two following strings join eachother:
#["cat" "dog"] ----> using print function we will get: catdog


#----------

#we can also put the values on the following lines (as long as they're in "[ ]" brackets)
#to make reading them as a "list" easier:

animals = ["cat", 
           "dog",
           "bird" ]


#------------------


#lists can also contain different data types!

movie_info = ["my bloody valentine", 1981]


#-------

#in python, counting of the ordered items starts from 0!

movies = ["the nun", "hobbit", "The conjuring", "Madea", "Friday the 13th", "HTTYD", "Star wars", "Rebels"]
# .          0 .          1 .          2  


#in the provided list we can see that "king-kong" is first, so its index number/address is 0
#the "hobbit" is 1, and so on and so forth


#---------------

#in a case where i just want to print only one value, i use the print function like normal:

print(movies)




#EXCEPT, this time i also put the index number of the value next to to the variable in [ ] :

print(movies[0])



#i can also do this in a different variable, as long as it's beside its original variable3

favourite = movies[0]

print(favourite)



#we can aslo use NEGATIVE numbers as indexes, to print a value starting from the last of the list!
#ALTHOUGH the count from the last will start from 1 instead of 0

print(movies[-2]) # will print hobbit



#in cases where we want to print values starting from first inlcuding third or fourth or so on...
#we write the print function as normal 
#EXCEPT in [ ] we write the index of the "starter value" and the NORMAL number of the "end value"    
#with   " : "    between them:

print(movies[0:3]) # 0 ---> the nun ;  //  3 ---> the conjuring ;


#by adding a third index in the print function we can print the values after the intended intervals


print(movies[0:8:2]) #the nun; the conjuring; Friday the 13th; star wars


#it gets printed like: [0] 1 [2] 3 [4] 5 [6] 7       
#(the ones i put in brackets in this comment get printed by the above print function)

#if we put 3 instead of 2:

print(movies[0:8:3]) 

#terminal will show: [0] 1 2 [3] 4 5 [6] 7


#----------- #5 classwork ( the rest were done previously)


favourite_brand = input("please enter your favourite car brand: ")

car_brands=["toyota", favourite_brand, "mercedes", "ford"]

print(car_brands[1])
