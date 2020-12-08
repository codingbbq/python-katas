"""
You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.

"""

def positive_sum(arr):
    return sum([item for item in arr if item > 0] , 0)


print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5])) # 13
print(positive_sum([-1,2,3,4,-5])) # 9

print(positive_sum([])) # 0

print(positive_sum([-1,-2,-3,-4,-5])) # 0


"""
Such expressions are called as generator expressions.
Userfull link : https://www.python.org/dev/peps/pep-0289/
They are a little confusing, however I think constant usage of such expressions will help me understand them better.

The function sum has a second argument "start" which returns the start value for sum or defaults to 0

"""