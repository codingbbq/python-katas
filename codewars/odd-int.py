"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

"""
def find_it(seq):
    hashMap = dict()
    for x in seq:
        if(x in hashMap):
            hashMap[x] += 1
        else:
            hashMap[x] = 1
    
    # print(hashMap) 
    # {1: 2, 2: 2, 3: 2, 20: 2, -1: 2, 4: 2, -2: 2, 5: 3}

    for key in hashMap:
        if(hashMap[key] % 2 == 1):
            return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))