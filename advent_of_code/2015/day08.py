class Solution2015:
    
    def puzzleone(self, inpt):
        sum = 0
        for x in inpt:
            # python 3: will print the raw string
            x = fr"{x}"
            # Raw string : count of raw string : evaluated string : count of evaluated string
            # print(f"{x} : {len((x))} : {eval(x)} : {len(eval(x))}")
            sum+= len(x) - len(eval(x))

        return sum

    def puzzletwo(self, inpt):
        sum = 0
        for x in inpt:
            # python 3: will print the raw string
            x = fr"{x}"
            
            # Instead of converting to the new condition, we directly just add the new formatted raw string
            # 2 => for the starting and ending "
            # " becomes \" so every occurrance is doubled
            # \ becomeas \\, even here occurrance is doubled
            # However we will eventually minus with the actual raw string, so it is easier to just do addition of the new strings.
            sum+= (2+x.count('\\')+x.count('"'))

        return sum

with open("./advent_of_code/2015/input/day08.txt", "r") as file:
    inpt = [line.rstrip() for line in file.readlines()]

    # puzzle1 = Solution2015().puzzleone(inpt)
    # print(puzzle1)

    puzzle2 = Solution2015().puzzletwo(inpt)
    print(puzzle2)
