class Solution2015:
    def paper_and_ribbon(self, inpt):
        total_paper = 0
        total_ribbon = 0
        for x in inpt:
            dim = [int(d) for d in x.split('x')]
            # # 2*l*w + 2*w*h + 2*h*l
            a = dim[0]*dim[1]
            b = dim[1]*dim[2]
            c = dim[2]*dim[0]
            
            # To find total wrapping paper
            small = min(a, b, c)
            sum_paper = 2*a + 2*b + 2*c + small
            total_paper+=sum_paper
            
            # To find ribbon

            # Sort the dim list to get min values
            dim.sort()
            present = 2*dim[0] + 2*dim[1]
            ribbon = dim[0]*dim[1]*dim[2]
            total_ribbon+= present+ribbon


        sol = {}
        sol["total paper"] = total_paper
        sol["total ribbon"] = total_ribbon
        return sol


files = open("./advent_of_code/2015/input/day02.txt", "r")
inpt = [line.rstrip() for line in files.readlines()]

puzzle = Solution2015().paper_and_ribbon(inpt)
print(puzzle)


