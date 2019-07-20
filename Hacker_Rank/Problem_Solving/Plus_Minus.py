import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    PCount, Ncount, ZCount = 0, 0, 0
    len_of_arr = len(arr)
    for num in arr:
        if num > 0:
            PCount += 1
        elif num < 0:
            Ncount += 1
        else:
            ZCount += 1
    print(PCount/len_of_arr)
    print(Ncount / len_of_arr)
    print(ZCount / len_of_arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
