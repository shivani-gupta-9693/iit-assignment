def binary_search(arr, n, k):
    arr.sort() 
    low = 0
    high = n - 1
     # Step 2: Iterative loop
    while low <= high:
        mid = (low + high) // 2
        # Check if k is at mid
        if arr[mid] == k:
            return 1
         # If k is greater, ignore left half
        elif arr[mid] < k:
            low = mid + 1
            
        # If k is smaller, ignore right half
        else:
            high = mid - 1
            
    # Step 3: If we reach here, the element was not present
    return -1
# Function ko test karne ke liye ye lines add karein
my_list = [2, 3, 4, 10, 40]
target = 10
n = len(my_list)

# Result ko print karein
print(binary_search(my_list, n, target))
