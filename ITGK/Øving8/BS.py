def binary_search(numbers, element):
    
    mid = len(numbers)//2
    if(len(numbers)==1 and numbers[0]!=element):return -float('inf')   
    if(numbers[mid]==element):return mid
    elif(numbers[mid]>element):return binary_search(numbers[:mid], element)
    else:return binary_search(numbers[mid+1:], element)
    

print(binary_search([1,2,3,4,5,6,7,8,9,10], 5))
    


