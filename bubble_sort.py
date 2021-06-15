#attempt the bubble sort

def bubsort(list):
    for h in range(len(list)-1):
        for i in range(len(list)-1-h):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list
    
print(bubsort([6,3,5,34,12,4,2,1,8]))