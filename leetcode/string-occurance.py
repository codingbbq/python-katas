# Find the count of substring in a string. The substring can overlap in a string like eg. below.
# Sample Input
# ABCDCDC
# CDC

# Sample Output
# 2

def count_substring(string, sub_string):
    count = 0
    for x in range(len(string)):
        if(string[x: x+len(sub_string)] == sub_string):
            count+=1
    
    return count

if __name__ == '__main__':
    count = count_substring("ABCDCDCYZ", "CDC")
    print(count)