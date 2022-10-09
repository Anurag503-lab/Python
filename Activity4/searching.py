#Write a program to perform searching activity using Linear and binary search.

def linear_Search(list1, n, key):
# Searching list1 sequentially
    for i in range(0, n):
        if (list1[i] == key):
            return i
        return -1
list1 = [1 ,3, 5, 4, 7, 9]
key = 7
n = len(list1)
res = linear_Search(list1, n, key)
if(res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)
    
    # Iterative Binary Search Function method Python Implementation
def binary_search(list1, n):
    low = 0
    high = len(list1) - 1
    mid = 0
    while low <= high:
        # for get integer result
        mid = (high + low) // 2
        # Check if n is present at mid
        if list1[mid] < n:
            low = mid + 1
        elif list1[mid] > n:   
            high = mid - 1
    # If n is smaller, compared to the left of mid
    else:
        return mid
    # element was not present in the list, return -1
    return -1
    list1 = [12, 24, 32, 39, 45, 50, 54]
    n = 45
    result = binary_search(list1, n)  
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in list1")