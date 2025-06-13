#hashmap
d = {"greg":1, "steve": 2, "rob": 3}

#add key value
d["arsh"]  = 4

# print(d)


# if "greg" in d:
#     print(True)



#loop over the key value pairs O(n)

# for key, val in d.items():
#     print(f"{key}: {val}")


#Default dict

from collections import defaultdict, Counter


# default  =defaultdict(int)

# print(default[2])

# print(default)



#default  =defaultdict(list)


#Counter
s = "aaaabbbbbcccccc"
counter  = Counter(s)
print(counter)