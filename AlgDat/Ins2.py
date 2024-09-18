def insertion_sort(A, n):
    l = [0]*n
    for i in range(n):
        temp = A[i]
        j = i
        while(j>0 and temp<l[j-1]):
            l[j] = l[j-1]
            j-=1
        l[j] = temp
    return l


l = [4, 3, 2, 1]
l = insertion_sort(l, len(l))
print(l)