import random

# Mengatur seed random
random.seed(40)

# Membuat 50 angka acak antara 0-100
numbers = [random.randint(0, 100) for _ in range(50)]

def merge_sort(arr):
    global comparisons
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    global comparisons
    merged = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        comparisons += 1
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

if __name__ == "__main__":
    comparisons = 0
    print("Array asli:", numbers, "\n")
    sorted_arr = merge_sort(numbers.copy())
    print("Array terurut:", sorted_arr, "\n")
    print("Jumlah perbandingan:", comparisons)
