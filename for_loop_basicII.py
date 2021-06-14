#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def bigSize(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i] = str("big")
    return list
print(bigSize([1, 4, -2, -5]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
def cp(list):
    count = 0
    for i in range(len(list)):
        if list[i]>0:
            count+=1
    list[len(list)-1] = count
    return list
print(cp([-1, 2, 3, -3, 5, 8, 3, 7]))

#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def st(list):
    sum = 0
    for i in list:
        sum+=i
    return sum
print(st([1,4,3,-9,45]))

#Average - Create a function that takes a list and returns the average of all the values.
def avg(list):
    sum = 0
    avg = 0
    for i in list:
        sum+=i
    avg = sum/len(list)
    return avg
print(avg([5,2,8,5,7,54,4]))

#Length - Create a function that takes a list and returns the length of the list.
def lol(list):
    lengthLol = len(list)
    return lengthLol
print(lol([48,38,6,3,6,8,3]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(list):
    if len(list) == 0:
        return False
    return min(list)
print(minimum([7,2,3,4,5]))
print(minimum([]))

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(list):
    if len(list) == 0:
        return False
    return max(list)
print(maximum([7,2,3,4,5]))
print(maximum([]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
def ua(list):
    myDictionary = {'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum':0, 'length': len(list)}
    for i in list:
        myDictionary['sumTotal']+=i
    myDictionary['average'] = myDictionary['sumTotal'] / len(list)
    myDictionary['minimum']= min(list)
    myDictionary['maximum']= max(list)
    return myDictionary
print(ua([3,6,3,6,7,9,45]))

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
def rl(list):
    for i in range(0, len(list)//2):
        temp = list[len(list)-1-i]
        list[len(list)-1-i] = list[i]
        list[i] = temp
    return list
print(rl([1,15,3,22,5,6,7]))

