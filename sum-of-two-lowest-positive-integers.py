"""
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. 
No floats or empty arrays will be passed.

"""
# Method 1
# In this approach, we change the original list, which is not recommended
def sum_two_smallest_numbers_long(numbers):
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    # We can use the sum function to iterate over a list. We can also use a tuple like below
    # return sum((min1, min2))
    return sum([min1,min2])


# Method 2
# Using the sort method to sort the list and then get the first two items from list
def sum_two_smallest_numbers(numbers):
    # In this approach, we sort the numbers list and then split the first two items, which we then sum.
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([5, 8, 12, 18, 22])) #13
print(sum_two_smallest_numbers([7, 15, 12, 18, 22])) #19
print(sum_two_smallest_numbers([25, 42, 12, 18, 22])) #30