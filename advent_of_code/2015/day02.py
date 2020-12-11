class Solution2015:
    def wrappingPaper(self, inpt):
        total_paper = 0
        for x in inpt:
            dim = [int(d) for d in x.split('x')]
            # # 2*l*w + 2*w*h + 2*h*l
            a = dim[0]*dim[1]
            b = dim[1]*dim[2]
            c = dim[2]*dim[0]
            small = min(a, b, c)
            sum_paper = 2*a + 2*b + 2*c + small
            total_paper+=sum_paper

        return total_paper

files = open("./advent_of_code/2015/input/day02.txt", "r")
inpt = [line.rstrip() for line in files.readlines()]

puzzle1 = Solution2015().wrappingPaper(inpt)
print(puzzle1)


