# 937. Reorder Data in Log Files
# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        index = 0
        # Take each list item and split and return whether it is digit or log
        
        for i, x in enumerate(logs):
            # Split the string on space and take the 0th element
            type  = x.split(" ")
            ind = logs[index].split(" ")

            if type[0][:3] == "dig":
                # Switch the places iff both x and ind are different
                if type[0][:3] != ind[0][:3]:
                    logs[index], logs[i] = logs[i], logs[index] 

            if type[0][:3] == "let":
                logs[index], logs[i] = logs[i], logs[index]
                index+=1

        # We have the index and we also have an unsorted array
        # Let us use quicksort to sort from 0 to index-1
        self.quickSort(logs, 0, index-1)
        return logs
        

    def quickSort(self, arr, start, end):
        if start >= end:
            return

        zIndex = self.partition(arr, start, end)
        self.quickSort(arr, start, zIndex-1)
        self.quickSort(arr, zIndex+1, end)
    
    def partition(self, arr, start, end):
        pivotIndex = start
        pivotValue = arr[end]
        for u in range(start, end):
            uVal = ord(arr[u].split(" ")[1][0])
            pVal = ord(pivotValue.split(" ")[1][0])
            if uVal < pVal:
                # Swap the values
                arr[u], arr[pivotIndex] = arr[pivotIndex], arr[u]
                pivotIndex+=1
        
        arr[pivotIndex], arr[end] = arr[end], arr[pivotIndex]
        return pivotIndex


sol = Solution().reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(sol)