"""
https://www.codewars.com/kata/find-the-middle-element/train/python

As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that 
lies between the other two elements.

The input to the function will be an array of three distinct numbers

"""

def gimme(input_array):
    # Create a new list
    sorted_array = list(input_array)
    # In place sorting
    sorted_array.sort()
    
    if(sorted_array[1] in input_array):
        return input_array.index(sorted_array[1])


print(gimme([2, 3, 1])) # 0, 'Finds the index of middle element'
print(gimme([5, 10, 14])) # 1, 'Finds the index of middle element'