"""
list:
    -contain duplicates
    -mutable -- we can modify, replace or delte the items
    -ordered -- maintain the order of elements based on how theu are added
    -accessing items in a list can be done directly using their position(index) starting from 0

    NB: List sotres references not values

"""

# a  = [10, 20, "GfG", 40, True]

# print(a)

#accessing elements using indexing
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])




#checking types of elements 
# print(type(a[2]))
# print(type(a[4]))





#Using the list constructor -> we can create a list by passing an iterable like a string, tuple, set or another list to the list fnction

#from a tuple
# a = list((1, 2, 3, "apple", 4.5))

# a = list([1, 2, 3, "apple", 4.5])

# a = list({1, 2, 3, "apple", 4.5})


# print(a)



##creating a list with repeated elements --> we can create a list with repeated elements by using the multiplciation operatpr
# #create a list [2, 2, 2, 2, 2]

# a  = [2] * 5
# b = [0] * 7

# print(a)
# print(b)



##adding elements into a list
#append : adds an element at  the end of the list
#extend: adds multille elements ot he end of a list
#insert: adds an element at a specific position

# a= []

#adding 10 to the end of the list
# a.append(10)
# print("After append(10): ", a)

#inserting 5 at index 0
# a.insert(0, 5)
# print("After insert (0, 5:)", a)


# Adding multiple elements  [15, 20, 25] at the end
# a.extend([15, 20, 25])
# print("After extend([15, 20, 25])", a)



##updating elements into list
# a  = [10, 20, 30, 40, 50]

#change the second element
# a[1] = 25

# print(a)


##Removing elements from a list

#remove -> remove the first occruence of an element
#pop -> remove the element at a specific index or the last element if no index is specified
#del statement -> deletes an element at a specified index

# a = [10, 20, 30, 40, 50]

#removes the first occurebce of 30
# a.remove(30)
# print("After remove 30: ", a)

#removes the element at index 1 (20)
# popped_val = a.pop(1)
# print("Popped element:", popped_val)
# print("After pop(1): ", a)


#deleted the forst elemet
# del a[0]
# print("After del a[0:]:", a)

#iterating over lists
#using a for loop

# a = ["apple", "banana", "cherry"]

# for item in a:
#     print(item)



#nested lists in python

matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

#access elemetn at row2, column 3
# print(matrix[1][2])

#create list of numbers with given range
r1= 0
r2 = 10

# li = list(range(r1, r2))
# print(li)


#using list comprehension
# li = [i for i in range(r1, r2)]
# print(li)

#using np.arange()
import numpy as np
# li = np.arange(r1, r2).tolist()

#using itertools.count()
import itertools
# li = list(itertools.islice(itertools.count(r1), r2-r1))
# print(li)

#ways to create a dictionary of lists 

#a--> Initialize a dictinalry of lists
# d = {}
# d["1"] = [1, 2]
# d["2"] = ["Geeks", "for", "Geeks"]
# print(d) 

#b--> Create a dictionary of lists using zip()
k = ["Fruits", "Vegetables", "Drinks"]
val = [["Apple", "Banana"], ["Carrot", "Spinach"], ["Water", "Juice"]]

#create a dictionary of lists using zip
# d = dict(zip(k, val))
# print(d)

#c--> Use defaultdict from collections defaultdict is a special kind of dictionary from the collections module in Python.
#It automatically gives a default value for a key that doesn’t exist, instead of giving an error.
# from collections import defaultdict
# d = defaultdict(list)
# d["fruits"].append("apple")
# d["fruits"].append("mango")
# d["veggies"].append("onion")
# d["veggies"].append("carrot")
# print(d)



#Create a list of tuples in python


