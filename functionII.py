#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countDown(num1):
    for i in range(num1, 0-1, -1):
        print(i)
countDown(10)
#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def pr(num1, num2):
    print(num1)
    return(num2)
print(pr(10, 32))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def fpl(list):
    sum = list[0] + len(list)
    return sum
print(fpl([10,35,35,6,43]))
#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def vgs(list):
    if len(list)<2:
        return False
    newList = []
    for i in list:
        if i>list[1]:
            newList.append(i)
    print(len(newList))        
    return newList
print(vgs([22, 24, 15, 34, 55, 16]))
print(vgs([22]))

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def LV(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(LV(4, 7))