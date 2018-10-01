from random import randint
import time




def erfen(ary,num):
    l = len(ary)
    low = 0
    high = l
    while low <= high:
        middle = (low + high) // 2
        if ary[middle] == num:
            return middle
        elif ary[middle] > num:
            high = middle
        else:
            low = middle
    return -1

if __name__ == '__main__':
    ary = [1,4,5,8,9,11,43,67,89]
    print(erfen(ary,11))








