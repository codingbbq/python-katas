
import re
class Solution2015:
    # Contains at least three vowels
    def vowels(self, s: str)-> bool:
        vowls = set('aeiou')
        p = 0
        for vow in s:
            if vow in vowls:
                p+=1

        if p >= 3:
            return True

    # Contains at least 2 in a row
    def twoinrow(self, s:str)-> bool:
       for i in range(1, len(s)):
           # Compare two consecutive strings
           if s[i-1] == s[i]:
               return True

    # Should not contain ab, cd, pq, or xy
    def shoulNotContain(self, s:str)-> bool:
        discard = ["ab", "cd", "pq", "xy"]
        for d in discard:
            if d in s:
                return False
        
        return True


    def nice(self, inpt):
        count = 0
        for x in inpt:
            if self.vowels(x) and self.twoinrow(x) and self.shoulNotContain(x):
                count+=1

        return count

    # Puzzle 2
    def pair(self, s):
        for i in range(len(s)-1):
            for j in range(i+2, len(s)-1):
                if s[i] == s[j] and s[i+1] == s[j+1]:
                    return True

    
    def exactMatch(self, s):
        for p in range(len(s)-2):
            if s[p] == s[p+2]:
                return True        

    def nicer(self, inpt):
        count = 0
        a = []
        for x in inpt:
            if self.pair(x) and self.exactMatch(x):
                count+=1

        return count   


files = open("./advent_of_code/2015/input/day05.txt", "r")
inpt = [line.rstrip() for line in files.readlines()]

# Nice strings
puzzle1 = Solution2015().nice(inpt)
print(puzzle1)

# Improved nicer strings
puzzle2 = Solution2015().nicer(inpt)
print(puzzle2)