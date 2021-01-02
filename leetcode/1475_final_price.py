# 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break

        return prices

sol = Solution().finalPrices(prices = [8,7,4,2,8,1,7,7,10,1])
print(sol)