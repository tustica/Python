#attempt a selection sort

def ss(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
                print(list[min])
        list[i], list[min] = list[min], list[i]
    return list
print(ss([3,2,5,87,54,7,4,3,44]))