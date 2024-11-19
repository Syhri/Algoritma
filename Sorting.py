# Syahril Fitrawan Abadi_F55123054

# MERGE SORT

import time

def merge_sort(arr):
    # Analisis merge sort:
    # Worst Case: O(n log n) - Terjadi pada semua kasus karena algoritma ini selalu membagi array menjadi dua bagian dan menggabungkannya kembali dengan cara yang hampir sama.
    # Best Case: O(n log n) - Sama seperti worst case, karena proses pembagian dan penggabungan tetap sama.
    # Average Case: O(n log n) - Sama seperti best case dan worst case, karena prosesnya konsisten.
    
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

# Expected Output Merge Sort:
# Sorted array using Merge Sort: [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9, 9]
# Merge Sort Time: 0.000072 seconds (berganti-ganti dan selalu lebih tinggi daripada quicksort untuk kasus data array X)

# QUICK SORT

def quick_sort(arr):
    # Analisis quick sort:
    # Worst Case: O(n^2) - Terjadi ketika pivot yang dipilih selalu elemen terkecil atau terbesar, seperti pada array yang sudah terurut atau terurut terbalik.
    # Best Case: O(n log n) - Terjadi ketika pivot yang dipilih selalu elemen median, membagi array menjadi dua bagian yang hampir sama.
    # Average Case: O(n log n) - Pada rata-rata, pivot yang dipilih akan membagi array menjadi dua bagian yang tidak terlalu tidak seimbang, sehingga kompleksitasnya mendekati O(n log n).
    
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

# Expected Output Quick Sort:
# Sorted array using Quick Sort: [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7, 7, 8, 9, 9]
# Quick Sort Time: 0.000035 seconds (berganti-ganti dan selalu lebih rendah daripada merge sort untuk kasus data array X)

# KESIMPULAN:
# Merge Sort memiliki kompleksitas waktu O(n log n) dalam kasus terbaik, rata-rata, dan terburuk.
# Quick Sort memiliki kompleksitas waktu O(n log n) dalam kasus terbaik dan rata-rata, tetapi O(n^2) dalam kasus terburuk.
# Quick Sort lebih cepat dalam pengujian ini, tetapi untuk data yang lebih besar atau dalam kasus terburuk, Merge Sort mungkin lebih stabil karena kompleksitas waktunya yang selalu O(n log n).