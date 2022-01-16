"""Subject: Advanced topics I: Efficiency
Project: writing the algorithm for binary search"""
import random
nums = [random.randint(0,20) for i in range(10)]

def binarySearch(aList,num):
    aList.sort()
    while aList:
        mid = len(aList)//2
        if aList[mid] == num:
            return True
        elif aList[mid] > num:
            aList = aList[:mid]
            print(aList)
        elif aList[mid] < num:
            aList = aList[mid+1:]

    return False



print(binarySearch(nums,3))
