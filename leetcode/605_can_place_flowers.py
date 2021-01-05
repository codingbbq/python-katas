# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # If there is just one flowerbed and it is empty, we can fill it
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        count = 0
        # Loop through the array and find all the empty flowerbeds in which flowers can be planted
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:

                # Check for 0th and n-1th positions
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count+=1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        count+=1
                else:
                # Check if previous is 0 and next is 0
                   if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count+=1

        if count >= n:
            return True

        return False


sol = Solution().canPlaceFlowers(flowerbed = [0], n = 2)
print(sol)