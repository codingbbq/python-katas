# 1436. Destination City
# https://leetcode.com/problems/destination-city/

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityA, cityB = set(), set()
        for x in paths:
            cityA.add(x[0])
            cityB.add(x[1])

        return (cityB - cityA).pop()



Solution().destCity(paths = [["B","C"],["D","B"],["C","A"]])