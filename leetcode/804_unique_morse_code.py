# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        strhash = {}
        for x in words:
            newstr = ''
            for l in x:
                newstr+= mc[ord(l) - 97]
            strhash[newstr] = strhash.setdefault(newstr, 0) + 1

        return len(strhash)


solution = Solution().uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"])
print(solution)