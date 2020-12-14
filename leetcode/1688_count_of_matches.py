# 1688. Count of Matches in Tournament
# https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            if n%2==0:
                n = n//2 
                count+= n
            else:
                n = ((n-1)//2)
                count+= n + 1

        return count

solution = Solution().numberOfMatches(n = 7)
print(solution)