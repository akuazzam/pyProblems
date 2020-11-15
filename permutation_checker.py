'''
Following code checks whether or not
two strings are permutaitons of one another
Not case sensetive
'''

def arePerms (str1, str2):
    if (len (str1) != len (str2)):
        return False
    # Create a histogram of str1 and cancel it out using str2
    # If there are any left overs, not permuations of each other
    histogram = [0 for i in range (0, 26)]
    
    for i in range (0, len (str1)):
        # creating a histogram for how many times each letter in str1 appears
        # subtracting 97 to normalize characters by taking the value of 'a' on each character
        # decrease each count of str2
        histogram[ord(str1[i].lower()) - 97] +=1
        histogram[ord(str2[i].lower()) - 97] -= 1

    #check if there are any leftovers
    for count in histogram:
        if count != 0:
            return False
    return True

#Tests
print(arePerms ("abc", "cba")) #True
print(arePerms ("lol", "llz")) #False
print(arePerms ("ABcd", "cBaD")) #True
print(arePerms ("", "")) #True
print(arePerms ("oofdf", "oofd")) #False