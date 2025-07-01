class Node:
    def __init__(self, data, next_node=None) -> None:  # next_node parameter should have default None
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, first_node) -> None:
        self.first_node = first_node

    #reading -> O(N)
    def read(self, index):
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            current_node = current_node.next_node
            current_index+=1

            if current_node is None:
                return None
        return current_node.data
    
    #searchingL O(n)
    def index_of(self, value):
        #we beginn at the first node of the list
        current_node  = self.first_node
        current_index = 0

        while current_node:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index +=1
        return None

    #Insertion
    def insert_at_index(self, index, value):
        #we create the newnode with the provided value
        new_node = Node(value)

        #if we are inserting in the beginning of the linkedlist
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        #if we are inserting anywhere other than the beginning
        current_node = self.first_node
        current_index = 0

        while current_index < index - 1:
            if current_node is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node
            current_index +=1

        #have the new node link point to the next node
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    #Deletion
    def delete(self, index):
        if index == 0:
            if self.first_node is not None:
                self.first_node = self.first_node.next_node
            return
        current_node = self.first_node
        current_index  = 0

        while current_index < (index - 1):
            if current_node is None or  current_node.next_node is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next_node
            current_index+=1
            
        #when we get to the node before the node to the deleted
        #access the link to the node after the node to be deleted

        if current_node.next_node is not None:
            node_after_deleted_node = current_node.next_node.next_node
            current_node.next_node = node_after_deleted_node
        else:
            raise IndexError("Index out of bounds")
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
# print(linked_list.read(0))
print(linked_list.index_of("time"))
linked_list.insert_at_index(3, "fucken")
print_list(linked_list)

linked_list.delete(3)
print_list(linked_list)