# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        # Break the string into two halves.
        l = len(s)//2
        a,b = s[:l], s[l:]
        vowels = ["a", "e", "i", "o", "u"]
        ai, bi = 0,0
        for i in range(l):
            if a[i].lower() in vowels:
                ai+=1
            if b[i].lower() in vowels:
                bi+=1
        
        if ai == bi:
            return True
        
        return False


sol = Solution().halvesAreAlike(s = "textbook")
print(sol)