from collections import deque

ordinals  = deque(["first", "second", "third"])

#rotate items to the right

# ordinals.rotate()


#rotate items to the elft
ordinals.rotate(-2)
print(ordinals)