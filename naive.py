import random

# Mengatur seed random
random.seed(40)

# Membuat 50 angka acak antara 0-100
numbers = [random.randint(0, 100) for _ in range(50)]

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Flag untuk optimasi jika array sudah terurut (kasus terbaik)
        swapped = False
        
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swaps += 1
        
        # Jika tidak ada pertukaran, array sudah terurut
        if not swapped:
            break
    
    return arr, comparisons, swaps

if __name__ == "__main__":
    print("Array asli:", numbers, "\n")
    sorted_arr, comparisons, swaps = bubble_sort(numbers.copy())
    print("Array terurut:", sorted_arr, "\n")
    print("Jumlah perbandingan:", comparisons, "\n")
    print("Jumlah pertukaran:", swaps)
