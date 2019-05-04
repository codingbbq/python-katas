"""
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. 
If the two numbers are equal return a or b.

"""

# Again this is a long form. We can still optimize this code by using min and max functions.
def get_sum_long(a,b):
    if(a > b):
        return sum(range(b, a+1))
    else:
        return sum(range(a, b+1))



# Method 2: We use the max and min functions
def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
    
print(get_sum(0,1)) #1
print(get_sum(0,-1)) #1