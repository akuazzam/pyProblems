'''
Following function checks if a word is a palindrome
Takes in user input
'''
def isPalindromic (word):
    for i in range (0, len (word) // 2):
        if (word[i].lower() != word[len(word) - 1 - i].lower()):
            return False
    return True
word = input("Enter a word you want to check: ")

if (isPalindromic (word)):
    print ("{} is a planindrome!".format(word))
else:
    print ("{} is not a palindrome".format(word))
