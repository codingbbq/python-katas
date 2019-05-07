"""
A string is considered to be in title case if each word in the string is either (a) capitalised 
(that is, only the first letter of the word is in upper case) or (b) considered to be an exception and put entirely 
into lower case unless it is the first word, which is always capitalised.

Write a function that will convert a string into title case, given an optional list of 
exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. 
Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.

"""
def title_case(title, minor_words = ""):
    if(title == ""):
        return ""
    else:
        title_list = title.lower().split()
        words_list = minor_words.lower().split()
        final_list = []
        for word in title_list:
            if(word in words_list):
                final_list.append(word)
            else:
                final_list.append(word.capitalize())
        
        final_list[0] = title_list[0].title()
        return " ".join(final_list)

print(title_case('a clash of KINGS', 'a an the of')) # should return: 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return: 'The Wind in the Willows'
print(title_case('the quick brown fox')) # should return: 'The Quick Brown Fox'