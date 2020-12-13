class Solution2015:

    def processStmt(self, instruction):
        ilist = instruction.split(" ")
        if ilist[0] == "turn" and ilist[1] == "on":
            return self.switch("on", ilist[2], ilist[4])

        if ilist[0] == "turn" and ilist[1] == "off":
            return self.switch("off", ilist[2], ilist[4])

        if ilist[0] == "toggle":
            return self.switch("toggle", ilist[1], ilist[3])

    # perform actions on the lights
    def switch(self, action, cX, cY):
        i = cX.split(',')
        xi, yi = i[0], i[1]

        j = cY.split(',')
        xj, yj = j[0], j[1]

        return xi


    def litLights(self, inpt):
        count = 0
        for stmt in inpt:
            return self.processStmt(stmt)
        

files = open("./advent_of_code/2015/input/day06.txt", "r")
inpt = [line.rstrip() for line in files.readlines()]

lightMatrix = []

puzzle1 = Solution2015().litLights(["turn on 0,0 through 999,999"])
print(puzzle1)