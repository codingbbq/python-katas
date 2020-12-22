# 477. Total Hamming Distance
# https://leetcode.com/problems/total-hamming-distance/

from typing import List

# Brute force approach which resulted in TLE
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        sum = 0
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                sum+=self.hammingDistance(nums[x], nums[y])
        return sum

    def hammingDistance(self, i, j):
        bin_i = bin(i).replace("0b", "")
        bin_j = bin(j).replace("0b", "")
        l = max(len(bin_i), len(bin_j))
        bin_i = str(bin_i).zfill(l)
        bin_j = str(bin_j).zfill(l)
        count=0
        for i in range(l):
            if int(bin_i[i]) - int(bin_j[i]) != 0:
                count+=1

        return count

sol = Solution().totalHammingDistance(nums = [4,14,2])
print(sol)