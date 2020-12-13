import hashlib

class Solution2015:

    def stockingStuffer(self, chars, startswith):
        i = 1
        while i < 9999999:
            md = chars + str(i)
            hash = hashlib.md5(md.encode('utf-8')).hexdigest()
            if hash.startswith(startswith):
                return i
            i+=1


# Input = bgvyzdsv
puzzle1 = Solution2015().stockingStuffer("bgvyzdsv", '00000')
print(puzzle1)

puzzle2 = Solution2015().stockingStuffer("bgvyzdsv", '000000')
print(puzzle2)