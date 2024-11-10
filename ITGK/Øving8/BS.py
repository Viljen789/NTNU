def binary_search(numbers, element):
    l = 0
    r = len(numbers)-1;
    while(l<=r):
        mid = l + (r-l)//2
        if(numbers[mid]==element):return mid
        elif(numbers[mid]<element):l = mid+1
        else: r = mid-1
    return -float("inf")


def rec_bs(lst, target):
    l = 0
    r = len(lst)-1
    mid = l + (r-l+1)//2
    if(lst[mid]==target):return mid
    if(r<=l):return -float("inf")
    elif(lst[mid]<target): return mid + rec_bs(lst[mid:], target)
    else: return rec_bs(lst[:mid], target)


        
l = [1, 3, 4, 5, 7, 8, 9, 10]
for i in range(11):
    print(f"Index of {i} is {binary_search(l, i)} and {rec_bs(l, i)}")

