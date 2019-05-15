"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built 
with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""

def is_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a): 
        return False
    else: 
        return True 


print(is_triangle(1, 2, 2)) #True
print(is_triangle(7, 2, 2)) #False
print(is_triangle(1, 2, 3)) #False
print(is_triangle(1, 3, 2)) #False
print(is_triangle(3, 1, 2)) #False
print(is_triangle(5, 1, 2)) #False
print(is_triangle(1, 2, 5)) #False
print(is_triangle(2, 5, 1)) #False
print(is_triangle(4, 2, 3)) #True
print(is_triangle(5, 1, 5)) #True
print(is_triangle(2, 2, 2)) #True
print(is_triangle(-1, 2, 3)) #False
print(is_triangle(1, -2, 3)) #False
print(is_triangle(1, 2, -3)) #False
print(is_triangle(0, 2, 3)) #False
