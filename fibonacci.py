"""
solves fib (n) in two ways: recursively and iteratively

fib series: 0, 1, 1, 2, 3, 5, 8, 11, ...
"""

def fib_itr (n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    a = 0
    b = 1
    c = 0
    for i in range (2, n + 1):
        c = a + b
        temp = b
        b = c
        a = temp
    return c

def fib_recur (n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib_recur (n-1) + fib_recur (n-2)

#test
print (fib_itr (5), fib_recur (5))
