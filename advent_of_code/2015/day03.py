class Solution2015:

    # Keeps track of the houses
    def drop_gift(self, houses, pos_x, pos_y):
        houses["{0}, {1}".format(pos_x, pos_y)] = houses.setdefault("{0}, {1}".format(pos_x, pos_y), 0) + 1
    
    
    # Puzzle 1
    def SantahouseVisited(self, instructions, houses, pos_x, pos_y):
        for x in instructions:
            if x == "^":
                pos_x+=1
                self.drop_gift(houses, pos_x, pos_y)
            if x == ">":
                pos_y+=1
                self.drop_gift(houses, pos_x, pos_y)
            if x == "v":
                pos_x-=1
                self.drop_gift(houses, pos_x, pos_y)
            if x == "<":
                pos_y-=1
                self.drop_gift(houses, pos_x, pos_y)

        return len(houses.keys())

    # Puzzle 2
    def SantaAndRobohouseVisited(self, instructions, houses, santa_pos_x, santa_pos_y, robo_pos_x, robo_pos_y):
        for i,x in enumerate(instructions):
            if(i%2==0):
                if x == "^":
                    santa_pos_x+=1
                    self.drop_gift(houses, santa_pos_x, santa_pos_y)
                if x == ">":
                    santa_pos_y+=1
                    self.drop_gift(houses, santa_pos_x, santa_pos_y)
                if x == "v":
                    santa_pos_x-=1
                    self.drop_gift(houses, santa_pos_x, santa_pos_y)
                if x == "<":
                    santa_pos_y-=1
                    self.drop_gift(houses, santa_pos_x, santa_pos_y)
            else:
                if x == "^":
                    robo_pos_x+=1
                    self.drop_gift(houses, robo_pos_x, robo_pos_y)
                if x == ">":
                    robo_pos_y+=1
                    self.drop_gift(houses, robo_pos_x, robo_pos_y)
                if x == "v":
                    robo_pos_x-=1
                    self.drop_gift(houses, robo_pos_x, robo_pos_y)
                if x == "<":
                    robo_pos_y-=1
                    self.drop_gift(houses, robo_pos_x, robo_pos_y) 
        
        return len(houses.keys())

f = open("./advent_of_code/2015/input/day03.txt", "r")
inpt = list(f.read().strip())
houses = {}
santa_pos_x, santa_pos_y, robo_pos_x, robo_pos_y = 0, 0, 0, 0
puzzle1 = Solution2015().SantahouseVisited(inpt, houses, santa_pos_x, santa_pos_y)
print(puzzle1)
houses = {}
puzzle2 = Solution2015().SantaAndRobohouseVisited(inpt, houses, santa_pos_x, santa_pos_y, robo_pos_x, robo_pos_y)
print(puzzle2)