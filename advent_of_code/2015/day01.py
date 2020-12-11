class Solution2015:
    
    def whichFloor(self, ipt):
        floor = 0
        for x in ipt:
            if x == "(":
                floor+=1
            
            if x == ")":
                floor-=1

        return floor

    def position(self, ipt):
        floor = 0
        for i, x in enumerate(ipt):
            if x == "(":
                floor+=1
            
            if x == ")":
                floor-=1

            if floor == -1:
                return i+1

        return True

files = open("./advent_of_code/2015/input/day01.txt", "r")
inpt = files.read()
puzzle1 = Solution2015().whichFloor(inpt)
print(puzzle1)

puzzle2 = Solution2015().position(inpt)
print(puzzle2)


