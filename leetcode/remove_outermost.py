# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt = 0
        Slist = list(S)
        NewList = []
        for i, x in enumerate(S):
            
            if cnt != 0 and not(cnt == 1 and x == ')'):
                NewList.append(x)

            if x == '(':
                cnt+=1
            else:
                cnt-=1

            

        return ''.join(NewList)


Solution().removeOuterParentheses(S = "(()())(())(()(()))")