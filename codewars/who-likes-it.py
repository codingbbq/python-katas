"""
https://www.codewars.com/kata/who-likes-it/train/python

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
"""

# Attempt 1:

# def likes(names):
#     sentence = "like this"
#     how_many = len(names)

#     if(how_many == 0):
#         return "no one likes this"
#     elif(how_many == 1):
#         return "{} likes this".format(names[0]) 
#     elif(how_many == 2):
#         return "{} and {} like this".format(names[0], names[1])
#     elif(how_many == 3):
#         return "{}, {} and {} like this".format(names[0], names[1], names[2])
#     else:
#         return "{}, {} and {} others like this".format(names[0], names[1], (len(names) - 2))   


# Better solution
def likes(names):

    # Create a dictionary with all possible formats
    formats = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }

    # Find the length of the inserted list of names
    n = len(names)


    # min(n,4) => If the length of list is more than 4, we return min which is 4.
    # *names => expands the list upto the number of variables required in format funcion
    return formats[min(n, 4)].format(*names, others=n-2)


print(likes([]))   # 'no one likes this'
print(likes(['Peter']))   # 'Peter likes this'
print(likes(['Jacob', 'Alex']))   # 'Jacob and Alex like this'
print(likes(['Max', 'John', 'Mark']))   # 'Max, John and Mark like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))   # 'Alex, Jacob and 2 others like this'