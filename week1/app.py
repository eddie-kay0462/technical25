"""
1) Set turotial with mosh
"""

# numbers = [1, 1, 2, 3, 4]
# first  = set(numbers) # {1, 2, 3, 4 }
# second = {1, 5}

# print(first | second)

# print(first & second)

# print(first - second)


# print( first ^ second ) #symmetric difference

# #Unlike lists, sets are undordered collection (sequence), and so we cant access them using an index. No duplciate values


"""
set tutorial with bro code
"""

utensils = {"fork", "spoon", "knife"}
dishes = { "bowl", "plate", "cup", "knife" }


# #add
# utensils.add("napkin")

# #remove
# utensils.remove("fork")

# #clear
# utensils.clear()

# dishes.update(utensils)

# dinner_table = utensils.union(dishes)


# for x in dinner_table:
#     print(x)

# print(dishes.difference(utensils))

print(utensils.intersection(dishes))
