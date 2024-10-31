def swap(a, b):
    return b, a

def bubble_sort(l):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = swap(l[i], l[i + 1])
                swapped = True
                
    return l
    



def selection_sort(l):
    sorted = True
    for i in range(len(l)):
        sorted = True
        min_index = i
        for j in range(i + 1, len(l)):
            if l[j] < l[min_index]:
                min_index = j
                sorted = False
        l[i], l[min_index] = swap(l[i], l[min_index])
        if(sorted):
            return l
    return l


print(selection_sort([5, 3, 8, 6, 7, 2]))