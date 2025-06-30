class Node:
    def __init__(self, data, next_node=None) -> None:  # next_node parameter should have default None
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, first_node) -> None:
        self.first_node = first_node

    def read(self, index):
        current_node =  self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index+=1

            if current_node is None:
                return None
        return current_node.data

#creating nodes
node_1 = Node("once")  # Now we can create nodes without the next_node parameter
node_2 = Node("upon")
node_3 = Node("a") 
node_4 = Node("time")


node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

#creating the linked list
linked_list = LinkedList(node_1)

#Function to print the list fromt he LinkedlIst class
def print_list(list_obj):
    current = list_obj.first_node
    while current:
        print(current.data, end="") 
        print(" -> ", end="") # Fixed spacing around ->
        current = current.next_node
        
    print("None")

print_list(linked_list)
print(linked_list.read(3))