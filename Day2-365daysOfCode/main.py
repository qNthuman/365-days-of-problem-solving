# Day2-365daysOfCode 
 AUTHOR = "Rmj"
"""

PS: Given an array of integers, calculate
the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each
fraction on a new line with  places after the decimal.

"""

import math
import os
import random
import re
import sys


def plusMinus(arr):
    cntps = 0
    cntNe = 0
    cntO = 0
    
    for i in arr:
        if i > 0:
            cntps+=1
        elif i < 0:
            cntNe+=1
        else:
            cntO+=1
            
    
    print("{0:5f}".format(cntps/len(arr)))
    print("{0:5f}".format(cntNe/len(arr)))
    print("{0:5f}".format(cntO/len(arr)))
    
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

