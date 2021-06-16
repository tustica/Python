#attempt an insertion sort

def insSort(list):
    for i in range(len(list)):
        for j in range(i):
            if list[i]<list[j]:
                list[i], list[j] = list[j], list[i]
                print(list)

    return list

print(insSort([3,2,5,87,54,7,4,3,44]))

#possibly more efficient way to do it//

def insSort(list):
    for i in range(len(list)):
        j = i
        while j>0 and list[j-1]>list[j]:
            list[j-1], list[j] = list[j], list[j-1]
            j-=1
    return list
print(insSort([3,2,5,87,54,7,4,3,44]))

#playing with ternary operaters
stacks = 2
# traditional
if stacks >= 3:
    print('Coding Dojo')
else:
    print('You are not Coding Dojo!')
# ternary
print('Coding Dojo' if stacks >= 3 else 'You are not Coding Dojo!')



