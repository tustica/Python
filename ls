[1mdiff --git a/for_loop_basicII.py b/for_loop_basicII.py[m
[1mnew file mode 100644[m
[1mindex 0000000..44e3ac7[m
[1m--- /dev/null[m
[1m+++ b/for_loop_basicII.py[m
[36m@@ -0,0 +1,78 @@[m
[32m+[m[32m#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".[m
[32m+[m[32mdef bigSize(list):[m
[32m+[m[32m    for i in range(len(list)):[m
[32m+[m[32m        if list[i]>0:[m
[32m+[m[32m            list[i] = str("big")[m
[32m+[m[32m    return list[m
[32m+[m[32mprint(bigSize([1, 4, -2, -5]))[m
[32m+[m
[32m+[m[32m#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).[m
[32m+[m[32mdef cp(list):[m
[32m+[m[32m    count = 0[m
[32m+[m[32m    for i in range(len(list)):[m
[32m+[m[32m        if list[i]>0:[m
[32m+[m[32m            count+=1[m
[32m+[m[32m    list[len(list)-1] = count[m
[32m+[m[32m    return list[m
[32m+[m[32mprint(cp([-1, 2, 3, -3, 5, 8, 3, 7]))[m
[32m+[m
[32m+[m[32m#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.[m
[32m+[m[32mdef st(list):[m
[32m+[m[32m    sum = 0[m
[32m+[m[32m    for i in list:[m
[32m+[m[32m        sum+=i[m
[32m+[m[32m    return sum[m
[32m+[m[32mprint(st([1,4,3,-9,45]))[m
[32m+[m
[32m+[m[32m#Average - Create a function that takes a list and returns the average of all the values.[m
[32m+[m[32mdef avg(list):[m
[32m+[m[32m    sum = 0[m
[32m+[m[32m    avg = 0[m
[32m+[m[32m    for i in list:[m
[32m+[m[32m        sum+=i[m
[32m+[m[32m    avg = sum/len(list)[m
[32m+[m[32m    return avg[m
[32m+[m[32mprint(avg([5,2,8,5,7,54,4]))[m
[32m+[m
[32m+[m[32m#Length - Create a function that takes a list and returns the length of the list.[m
[32m+[m[32mdef lol(list):[m
[32m+[m[32m    lengthLol = len(list)[m
[32m+[m[32m    return lengthLol[m
[32m+[m[32mprint(lol([48,38,6,3,6,8,3]))[m
[32m+[m
[32m+[m[32m#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.[m
[32m+[m[32mdef minimum(list):[m
[32m+[m[32m    if len(list) == 0:[m
[32m+[m[32m        return False[m
[32m+[m[32m    return min(list)[m
[32m+[m[32mprint(minimum([7,2,3,4,5]))[m
[32m+[m[32mprint(minimum([]))[m
[32m+[m
[32m+[m[32m#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.[m
[32m+[m[32mdef maximum(list):[m
[32m+[m[32m    if len(list) == 0:[m
[32m+[m[32m        return False[m
[32m+[m[32m    return max(list)[m
[32m+[m[32mprint(maximum([7,2,3,4,5]))[m
[32m+[m[32mprint(maximum([]))[m
[32m+[m
[32m+[m[32m#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.[m
[32m+[m[32mdef ua(list):[m
[32m+[m[32m    myDictionary = {'sumTotal': 0, 'average': 0, 'minimum': 0, 'maximum':0, 'length': len(list)}[m
[32m+[m[32m    for i in list:[m
[32m+[m[32m        myDictionary['sumTotal']+=i[m
[32m+[m[32m    myDictionary['average'] = myDictionary['sumTotal'] / len(list)[m
[32m+[m[32m    myDictionary['minimum']= min(list)[m
[32m+[m[32m    myDictionary['maximum']= max(list)[m
[32m+[m[32m    return myDictionary[m
[32m+[m[32mprint(ua([3,6,3,6,7,9,45]))[m
[32m+[m
[32m+[m[32m#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)[m
[32m+[m[32mdef rl(list):[m
[32m+[m[32m    for i in range(0, len(list)//2):[m
[32m+[m[32m        temp = list[len(list)-1-i][m
[32m+[m[32m        list[len(list)-1-i] = list[i][m
[32m+[m[32m        list[i] = temp[m
[32m+[m[32m    return list[m
[32m+[m[32mprint(rl([1,15,3,22,5,6,7]))[m
[32m+[m
