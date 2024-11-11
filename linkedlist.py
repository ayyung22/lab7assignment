#CIS 103 XY Fundamentals of Programming
#Lab 7: Lab Implementing and Manipulating Arrays
#Author: Annie Yung
#Date: 11/10/2024

class Node:
    def __init__(self, data=None):
        #Initialize the node with data and set the next pointer to None
        self.data = data
        self.next = None

    def __repr__(self):
        #Return a string representation of the node
        return f"Node(data={self.data})"


class LinkedList:
    def __init__(self):
        #Initialize an empty linked list with no nodes
        self.head = None

    def __repr__(self):
        #String representation of the linked list
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes)

    def insert_at_beginning(self, data):
        #Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        #Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            # Traverse the list to find the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def traverse(self):
        #Traverse the list and print the data of each node
        current = self.head
        if not current:
            print("The list is empty.")
            return

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  #Denotes that this is the end of the list

    def search(self, data):
        #Search for a node in the list."""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

#Creating nodes
node1 = Node(0)
node2 = Node(5)
node3 = Node(10)

# Link the nodes together
node1.next = node2  # node1 points to node2
node2.next = node3  # node2 points to node3

# Print the nodes and their next pointers
print(node1)
print(f"node1.next: {node1.next}")
print(f"node2.next: {node2.next}")
print(f"node3.next: {node3.next}")

#LinkedList class example
linked_list = LinkedList()

# Insert at the beginning
linked_list.insert_at_beginning(0)
linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(10)

print("LinkedList after insertions at the beginning:")
print(linked_list)  # Output would be 0 -> 5 -> 10

# Insert at the end
linked_list.insert_at_end(15)
linked_list.insert_at_end(20)

print("\nLinkedList after insertions at the end:")
print(linked_list)  # Output would be 0 -> 5 -> 10 -> 15 -> 20

# Testing the LinkedList class with traverse and search methods
linked_list = LinkedList()

# Insert some nodes
linked_list.insert_at_end(0)
linked_list.insert_at_end(5)
linked_list.insert_at_end(10)
linked_list.insert_at_beginning(-5)

# Traverse the list
print("Traversing the list:")
linked_list.traverse()  # Output: -5 -> 0 -> 5 -> 10 -> None

# Search for a node
search_result = linked_list.search(5)
if search_result:
    print("\nSearch result: Found node with data:", search_result)
else:
    print("\nSearch result: Node not found.")
