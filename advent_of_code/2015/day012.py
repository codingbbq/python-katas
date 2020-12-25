import json

class Solution2015:

    # Function to add all the int inside a dict
    def checkDict(self, dct,  ans):

        # This is for puzzle 2, remove the if condition to get answer for puzzle 1
        if "red" not in dct.values(): 
            for key, val in dct.items():
                if isinstance(val,  dict):
                    ans = self.checkDict(val, ans)
                
                elif isinstance(val, list):
                    ans = self.checkList(val,  ans)

                elif isinstance(val, int):
                    ans+=val

        return ans

    # Function to add all the int inside a list
    def checkList(self, lst, ans):

        for i in lst:
            if isinstance(i, int):
                ans+=i
                
            if isinstance(i, list):
                ans = self.checkList(i, ans)
            
            if isinstance(i, dict):
                ans = self.checkDict(i, ans)

        return ans
    
    def findSum(self, pydict, ans):
        if isinstance(pydict, int):
            ans+=pydict

        if isinstance(pydict, list):
            ans+=self.checkList(pydict, ans) 

        if isinstance(pydict, dict):
            ans+=self.checkDict(pydict, ans)
        return ans

with open("./advent_of_code/2015/input/day012.txt", "r") as file:
    inpt = [line.rstrip() for line in file.readlines()]
    # Convert the json object into a dict
    pydict = json.loads(inpt[0])
    ans = 0
    puzzle1 = Solution2015().findSum(pydict, ans)
    print(puzzle1)

    # For puzzle2, an if condition is added to find a value while checking if input is of type dict.
