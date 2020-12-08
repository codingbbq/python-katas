# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        result:str = ''
        for i in range(len(command)):
            if command[i] == 'G':
                result+= 'G'
            
            # Loop through n-1 items as we do not want to overflow
            if i < len(command):
                if command[i] == '(' and command[i+1] == ")":
                    result+= 'o'

                # Straight forward check 
                if command[i] == '(' and command[i+1] == 'a':
                    result+= 'al'

        return result

Solution().interpret(command = "G()()()()(al)")

# Gooooal