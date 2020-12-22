# To get all the permutations in the given towns
import itertools as it

class Solution2015:
    
    # Processing of the statement using the split method
    def processInput(self, instructions):
        s = instructions.split("=")
        towns = [x.strip() for x in s[0].split("to")]
        dist = s[1].strip()
        # This will return a tuple such as (["townA", "townB"], 30)
        return (towns, dist)


    def getCostPath(self, inpt, shortPath=True):
        # This will store all the path and its cost
        dict = {}

        # So that we can use in the permutations
        unique_towns = []
        for i, x in enumerate(inpt):
            y = self.processInput(x)
            towncomboA, towncomboB = str(y[0][0]) + str(y[0][1]), str(y[0][1]) + str(y[0][0])
            dict[towncomboA], dict[towncomboB] = y[1], y[1]

            # Using extend, we are storing all the towns in a single list
            unique_towns.extend(y[0])

        # Use set to get unique values of all the towns. i.e It will return total 8 items.
        # We convert it into a list and then in turn get all the permutations of the above list containing 8 towns
        all_routes = list(it.permutations(list(set(unique_towns))))
        cost = 0
        for k in all_routes:
            distance = 0
            for i in range(len(k) - 1):

                # We check the combination of two towns so that we can get the cost.
                if str(str(k[i]) + str(k[i+1])) in dict:
                    distance+= int(dict[str(str(k[i]) + str(k[i+1]))])
                else:
                    # If the town mapping is not available for we return distance as -1 and exit.
                    distance = -1
                    break
            
            # For the first run
            if cost == 0 and distance > 0:
                cost = distance

            # The flag which will determine if we want shortest path or the longest path
            if shortPath:
                if distance > 0 and distance < cost:
                    cost = distance
            else:
                if distance > 0 and distance > cost:
                    cost = distance

        return cost

with open("./advent_of_code/2015/input/day09.txt", "r") as file:
    inpt = [line.rstrip() for line in file.readlines()]

    puzzle1 = Solution2015().getCostPath(inpt, True)
    print(puzzle1)

    puzzle2 = Solution2015().getCostPath(inpt, False)
    print(puzzle2)
