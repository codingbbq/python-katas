# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert s into a list
        x = s.strip().split(" ")
        # Loop through each item in the list
        for i in range(len(x)):
            # Conver each word into another list
            rev  = [a for a in x[i]]
            # Reverse the order of each character
            start = 0
            end = len(rev) - 1
            while start < end:
                rev[start], rev[end] = rev[end], rev[start]
                start+=1
                end-=1
            x[i] = ''.join(rev)

        ans =  " ".join(x)
        return ans

sol = Solution().reverseWords(s = "Let's take LeetCode contest")
print(sol)