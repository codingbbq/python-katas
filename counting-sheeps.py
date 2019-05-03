"""
Consider an array of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

"""
def count_sheeps_long(arrayOfSheeps):
    countOfSheep = 0
    for sheep in arrayOfSheeps:
        if(sheep):
            countOfSheep += 1
    
    return countOfSheep


"""
A better solution I found on codewars was as below
by using the count function on the list.

"""

def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print(count_sheeps(array1))