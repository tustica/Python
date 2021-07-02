import unittest

def reverseList(list):
    for i in range(len(list)//2):
        list[i], list[len(list)-i-1] = list[len(list)-i-1], list[i]
    return list

print(reverseList([1,2,3,4,5,8,12]))