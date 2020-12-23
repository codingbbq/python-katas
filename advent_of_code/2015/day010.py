# Brute force approach. I could not figure out any algorithm ATM
class Solution2015:

    '''
    This function returns the new look and say number
    '''
    def lookAndSay(self, inpt, repeat):
        # The new number in list
        new_number = []
        # temp will keep track of the new number in a sequence.
        temp = []
        # To get started, insert first digit in temp list
        temp.append(inpt[0])
        count = 0
        for x in inpt:
            # For each dijit we check with temp[0]. If it matches we increase the count
            if temp[0] == x:
                count+=1
            else:
            # If the number does not match with temp[0], we first return whatever we have found out. i.e the count followed by number
                new_number.append(str(count))
                new_number.append(str(temp[0]))
            # Reset everything
                count = 1
                temp[0] = x

        # This is for the last digit in the number
        new_number.append(str(count))
        new_number.append(str(temp[0]))

        number =  ''.join(new_number)

        # Call the function n times
        if repeat > 0:
            repeat-=1
            return self.lookAndSay(number, repeat)

        return len(number)

inpt = "1113122113"
# Repeat 40 times. 
puzzle1 = Solution2015().lookAndSay(inpt, repeat=39)
print(puzzle1)

# Repeat 50 times.
puzzle2 = Solution2015().lookAndSay(inpt, repeat=49)
print(puzzle2)