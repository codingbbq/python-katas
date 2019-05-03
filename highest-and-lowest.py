"""
You are given a string of space separated numbers, and have to return the highest and lowest number.

"""
def high_and_low(numbers):
    
    results = numbers.split(" ")
    results = list(map(int, results))
    print("{} {}".format(max(results), min(results)))


high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
high_and_low("1") # return "1 1"