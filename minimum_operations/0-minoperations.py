#!/usr/bin/python3

def minOperations(n):
    #number to increment to n
    m = 1
    #used for increment
    x = 1
    #Operations count starts at 1 to account for the initial copy
    operationsCount = 0
    i = 1
    for i in range(n):
        if ((n % m) == 0):
            x = m
            operationsCount +=1
            m = m + x
            operationsCount +=1
        else:
            while ((n % m) != 0):
                m = m + x
                operationsCount +=1
        
        if (m == n):
            return operationsCount
        if (m > n):
            return 0
        
print(minOperations(12))