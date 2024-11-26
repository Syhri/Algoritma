# MERGE SORT

import time

def merge_sort(arr):
    
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

X = [1, 5, 6, 4, 3, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

start_time = time.time()
sorted_X_merge = merge_sort(X.copy())
merge_sort_time = time.time() - start_time

print("Sorted array using Merge Sort:", sorted_X_merge)
print("Merge Sort Time: {:.6f} seconds".format(merge_sort_time))

# QUICK SORT

def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

start_time = time.time()
sorted_X_quick = quick_sort(X.copy())
quick_sort_time = time.time() - start_time

print("Sorted array using Quick Sort:", sorted_X_quick)
print("Quick Sort Time: {:.6f} seconds".format(quick_sort_time))