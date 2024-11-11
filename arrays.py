#CIS 103 XY Fundamentals of Programming
#Lab 7: Lab Implementing and Manipulating Arrays
#Author: Annie Yung
#Date: 11/10/2024

class Array:
    def __init__(self, capacity, fill_value):
        # Initialize the array with given capacity and fill_value
        self.array = [fill_value] * capacity

    def __repr__(self):
        # String representation of the array
        return f"Array({self.array})"

    def insert(self, index, value):
        #Inserts a value at the specified index
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of bounds")

        # Insert value at the specified index
        self.array.insert(index, value)

    def delete(self, index):
        #Deletes the element at the specified index
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")

        # Delete the element at the specified index
        del self.array[index]

    def increase_size(self):
        #Increases the array size#
        #Create a new list with double the current size
        new_capacity = len(self.array) * 2
        self.array.extend([None] * (new_capacity - len(self.array)))
        print(f"Increased size to {new_capacity}.")

    def decrease_size(self):
        #Decreases the array size
        # Create a new list with half the current size
        new_capacity = max(1, len(self.array) // 2)
        self.array = self.array[:new_capacity]
        print(f"Decreased size to {new_capacity}.")


#Example of initial array
arr = Array(5, 0)  # Initialize an array with capacity of 5 and filled with zeros
print("Initial Array:", arr)
print()

# Insert value 5 at index 2
arr.insert(2, 5)
print("Array after insert:", arr)
print()

# Delete element at index 3
arr.delete(3)
print("Array after deleting index 3:", arr)
print()

#Increase size
arr.increase_size()
print("Array after increasing size:", arr)
print()
print()

# Decrease the size of the array
arr.decrease_size()
print("Array after decreasing size:", arr)


