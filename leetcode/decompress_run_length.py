# 1313. Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # The result list
        result = []
        for i,x in enumerate(nums):
            # We want 0th, 2nd i.e all even indices to find the frequency
            if(i%2 == 0):
                # x is the frequency, so loop over it and append (i+1)th item
                for j in range(x):
                    result.append(nums[i+1])

        return result


Solution().decompressRLElist(nums = [1,1,2,3])