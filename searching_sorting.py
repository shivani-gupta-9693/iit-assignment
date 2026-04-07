# 1. Insertion Sort Function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Elements ko aage shift karna jo key se bade hain
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 2. Iterative Binary Search
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid # Index return karega
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 3. Recursive Binary Search
def recursive_binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return recursive_binary_search(arr, mid + 1, high, target)
        else:
            return recursive_binary_search(arr, low, mid - 1, target)
    else:
        return -1

# --- Driver Code (Program yahan se start hoga) ---

arr = [8, 3, 6, 1, 9, 4]
target = 6

# Step 1: Sort the array
sorted_arr = insertion_sort(arr)
print(f"Sorted Array: {sorted_arr}")

# Step 2: Iterative Search
idx_iterative = iterative_binary_search(sorted_arr, target)
print(f"Iterative Binary Search Result: {idx_iterative}")

# Step 3: Recursive Search
idx_recursive = recursive_binary_search(sorted_arr, 0, len(sorted_arr) - 1, target)
print(f"Recursive Binary Search Result: {idx_recursive}")

# Final Output Message
if idx_iterative != -1:
    print(f"\nTarget {target} found at index {idx_iterative}")
else:
    print(f"\nTarget {target} not found")  