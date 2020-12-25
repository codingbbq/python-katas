'''
The Commented code is my attempt which I tried for almost 4-5hrs. 
I hit the recursion limit and I failed at it.
'''


# # Day 11
# # The input/output will be only 8 characters all lowercase letters
# # Increment one at a time just like numbers
# import sys
# x=30000
# sys.setrecursionlimit(x)

# class Solution2015:

#     def generatePassword(self, inpt, whichLetter):
#         inc = False
#         # First convert string to list
#         newInpt = list(inpt)

#         # Increment the last letter
#         letter = ord(newInpt[whichLetter])
#         if letter+1 == 105 or letter+1 == 108 or letter+1 == 111:
#             letter+=2
#         else:
#             if letter == 122: # Our letter is z
#                 letter = 97 # Switch it to a

#                 # we need a mechanism to increment the previous letter.
#                 # Increment the 6th position
#                 inc = True
#             else:
#                 letter+=1

#         # We have incremented the letter
#         newInpt[whichLetter] = chr(letter)
#         newInpt = "".join(newInpt)
#         if inc:
#             return self.generatePassword(newInpt, whichLetter-1)

#         # Check if the new password generated is valid
#         valid = self.checkValid(newInpt)
#         if not valid:
#             return self.generatePassword(newInpt, 7)
            
#         return newInpt
            
    
#     def corporatePassword(self, inpt):
#         # Generate a new password first
#         new_password = self.generatePassword(inpt, 7)
#         return new_password

#     def checkValid(self, chkInpt):
#         count=0
#         v = False
#         for j in range(1, len(chkInpt) - 1):
#             # Check for at least two overlapping letters
#             if chkInpt[j] == chkInpt[j+1] and chkInpt[j-1] != chkInpt[j]:
#                 count+=1
#             # Check for increasing straight of at least 3 letters
#             if (ord(chkInpt[j-1]) + 1) == ord(chkInpt[j]) == (ord(chkInpt[j+1]) - 1):
#                 v = True
        
#         if count >= 2 and v:
#             return True
#         print(chkInpt)
#         return False

# inpt = "abcdffgh"
# puzzle1 = Solution2015().corporatePassword(inpt)
# print(puzzle1)

# Solution taken from Reddit
def check(s):
    if( 'i' in s or 'o' in s or 'l' in s):
        return 0
    count = 0
    flag = 0
    char = ""
    for i in range(len(s)-1):
        if(s[i] == s[i+1] and s[i] not in char):
            count += 1
            char += s[i]
    for i in range(len(s)-2):
        if(s[i] == chr(ord(s[i+1])-1) and s[i+1] == chr(ord(s[i+2])-1)):
            flag = 1
    if(count >= 2 and flag == 1):
        return 1
    else:
        return 0

def gen(s):
    temp = ""
    if( (ord(s[len(s)-1]) - 96) == 26 ):
        temp += gen(s[:len(s)-1]) + "a"
    else:
        return (s[:len(s)-1] + chr(ord(s[len(s)-1])+1))
    return temp

test = 0
# Puzzle 1 input
string = "hepxcrrq"
# Puzzle 2 input
string = "hepxxyzz"
while(test == 0):
    string = gen(string)
    if(check(string)):
        print("yes")
        test = 1
print(string)