class Solution2015:
    MAX = 1000

    # Function to process the statements and extract data to be used later.
    def processStmt(self, instruction):
        
        ilist = instruction.split(" ")
        processedData = {}
        if ilist[0] == "turn" and ilist[1] == "on":
            x = ilist[2].split(',')
            y = ilist[4].split(',')
            processedData["action"] = "on"
            processedData["cX"] = [x[0], x[1]]
            processedData["cY"] = [y[0], y[1]]
            return processedData

        if ilist[0] == "turn" and ilist[1] == "off":
            x = ilist[2].split(',')
            y = ilist[4].split(',')
            processedData["action"] = "off"
            processedData["cX"] = [x[0], x[1]]
            processedData["cY"] = [y[0], y[1]]
            return processedData
            
        if ilist[0] == "toggle":
            x = ilist[1].split(',')
            y = ilist[3].split(',')
            processedData["action"] = "toggle"
            processedData["cX"] = [x[0], x[1]]
            processedData["cY"] = [y[0], y[1]]
            return processedData

    def litLights(self, inpt):
        # Let us turn off all the lights
        lightMatrix = []
        lightMatrix = [[0 for i in range(self.MAX)] for j in range(self.MAX)]
        count = 0
        for stmt in inpt:
            data = {}
            data = self.processStmt(stmt)
            for i in range(int(data['cX'][0]), 1 + int(data['cY'][0])):
                    for j in range(int(data['cX'][1]), 1 + int(data['cY'][1])):
                        if data["action"] == "on":
                            if lightMatrix[i][j] == 0:
                                lightMatrix[i][j] = 1
                                count+=1
                        if data["action"] == "off":
                            if lightMatrix[i][j] == 1:
                                lightMatrix[i][j] = 0
                                count-=1
                        if data["action"] == "toggle":
                            if lightMatrix[i][j] == 1:
                                lightMatrix[i][j] = 0
                                count-=1
                            else:
                                lightMatrix[i][j] = 1
                                count+=1

        return count

    def brightness(self, inpt):
        # Let us turn off all the lights
        lightMatrix = []
        lightMatrix = [[0 for i in range(self.MAX)] for j in range(self.MAX)]
        count = 0
        for stmt in inpt:
            data = {}
            data = self.processStmt(stmt)
            for i in range(int(data['cX'][0]), 1 + int(data['cY'][0])):
                    for j in range(int(data['cX'][1]), 1 + int(data['cY'][1])):
                        if data["action"] == "on":
                            lightMatrix[i][j]+= 1
                            count+=1

                        if data["action"] == "off":
                            if lightMatrix[i][j] > 0:
                                lightMatrix[i][j] -= 1
                                count-=1
                                
                        if data["action"] == "toggle":
                            lightMatrix[i][j] += 2
                            count+=2

        return count

files = open("./advent_of_code/2015/input/day06.txt", "r")
inpt = [line.rstrip() for line in files.readlines()]
puzzle1 = Solution2015().litLights(inpt)
print(puzzle1)

puzzle2 = Solution2015().brightness(inpt)
print(puzzle2)

files.close()