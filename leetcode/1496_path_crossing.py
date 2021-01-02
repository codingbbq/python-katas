# 1496. Path Crossing
# https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Coordinates
        p  = (0,0)
        # We are using set to store the visited nodes
        pathset = set()
        pathset.add(p)
        
        for i in path:
            if i == "N":
                p = (p[0], p[1]+1)
            if i == "E":
                p = (p[0]+1, p[1])
            if i == "S":
                p = (p[0], p[1]-1)
            if i == "W":
                p = (p[0]-1, p[1])

            if p in pathset:
                return True
            else:
                pathset.add(p)

        return False

sol = Solution().isPathCrossing(path = "NESWW")
print(sol)