from collections import deque


#Cwe can instantiate a deque with a list . 
# numbers = [1,2,3,4,5]
# deque_numbers = deque(numbers)

# #we can also instantiate a deque with a tuple
# numbers = (1,2,3,4,5)
# deque_numbers = deque(numbers)

# #we can also instantiate a deque with a set
# numbers = {1,2,3,4,5}



#popping and appending elements efficiently
numbers = deque([1,2,3,4])

# res  = numbers.popleft()
# print(res)

numbers.appendleft(0)
print(numbers)