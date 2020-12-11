# 1309. Decrypt String from Alphabet to Integer Mapping
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = { "1" : "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", "9": "i"}
        bet = { "10": "j", "11": "k", "12": "l", "13": "m", "14":"n", "15": "o", "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", "23": "w", "24": "x", "25": "y", "26": "z"}
        i = 0
        ans = []
        while i < len(s):
                if i+2 <= len(s)-1 and s[i+2] == "#" and str(s[i]) + str(s[i+1]) in bet:
                    ans.append(bet[str(s[i]) + str(s[i+1])])
                    i+=3
                elif s[i] in alpha:
                    ans.append(alpha[s[i]])
                    i+=1
        return ''.join(ans)
        

Solution().freqAlphabets(s = "25#")