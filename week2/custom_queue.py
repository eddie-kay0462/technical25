"""
Suppose you need a custom queue abstrract data type that ptovices onlthe following features:

- enqueue: add an element to the end of the queue
- dequeue: remove an element from the front of the queue
- size: return the number of elements in the queue
- Supporting membership tests
- Support normal and reverse iteration
- providing a string representation of the queue
"""

from collections import deque

class Queue:
    def __init__(self) -> None:
        self._items  = deque()


    def enqueue(self, item):
        self._items.append(item)
    
    def dequeue(self):
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None
        
    def __len__(self):
        return len(self._items)
    
    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        yield from self._items

    
    def __reversed__(self):
        yield from reversed(self._items)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"
    

numbers  = Queue()

# print(numbers)

#enuqueue items
for number in range(1, 5):
    numbers.enqueue(number)

# print(numbers)

#support len
length_q = len(numbers)
# print(length_q)

#Suppport membership tests
print(2 in numbers)  #automatically calls contains


#normal iteration
for number in reversed(numbers):
    print(f"Number: {number}")