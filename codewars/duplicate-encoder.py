"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once 
in the original string, or ")" if that character appears more than once in the original string. 
Ignore capitalization when determining if a character is a duplicate.

"""

# Attept 1
"""
The approach we have taken is, we create a hashtable and then assign values accordingly. 
Then we print the values
So we are using two for loops for this, which is not a good solution.
"""
def duplicate_encode_long(word):
    d = dict()
    ret = ""
    for x in word.lower():
        if(x in d):
            d[x] = ")"
        else:
            d[x] = "("
    
    for x in word.lower():
        ret += d[x]

    return ret



"""
Another good approach was to use the count() method and do the entire decoding in one loop
"""
def duplicate_encode(word):
    word = word.lower()
    result = ""
    for x in word:
        if word.count(x) > 1:
            result += ")"
        else:
            result += "("

    return result
    
print(duplicate_encode("din"))  # "((("
print(duplicate_encode("recede"))  # "()()()"
print(duplicate_encode("Success"))  # ")())())"
print(duplicate_encode("(( @"))  # "))(("