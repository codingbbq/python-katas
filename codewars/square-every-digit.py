"""
In this kata, you are asked to square every digit of a number.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
Note: The function accepts an integer and returns an integer

"""

# Attempt 1 
"""
In the below solution, we get each digit from the number by % 10 followed by / 10.
However in python /10 returns either a float of int. So we had to convert each result to int.
Apart from that, we are using a list to store each digit, which we need to then reverse 
before we join them. The join function returns of type str, so we need to again convert to int.
"""
def square_digits_long(num):
    squared = []
    while num > 0:
        n = num % 10
        squared.append(n**2)
        num = int(num/10)
        
    squared.reverse()
    return int("".join(map(str, squared)))



# Clever solution
"""
Below was a clever solution I found on codewars.
In below solution we do a lot of type conversion.

"""
def square_digits(num):
    ret = ""
    for digit in str(num):
        ret += str(int(digit)**2)
    return int(ret)

print(square_digits(9119)) # 811181