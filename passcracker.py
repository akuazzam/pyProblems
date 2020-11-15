'''
following code prints out all the possilble alphabetic combination for string length of n
characters are limited to a-z for now
'''

def print_all_combs (n):
    def print_combs_recur (str):
        if (len (str) == n):
            print (str)
        else:
            for i in range (0, 26):
                print_combs_recur (str + chr (ord ('a') + i))
    print_combs_recur ("")

# print all the possible 4 letter words using [a-z]
print_all_combs (4)
