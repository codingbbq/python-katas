#Leetcode : 771. Jewels and Stones
#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for jewel in J:
            for stones in S:
                if jewel == stones: 
                    count+=1
            
        print(count)


Solution().numJewelsInStones(J = "aA", S = "aAAbbbb")