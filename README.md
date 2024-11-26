B_Syahril Fitrawan Abadi_F55123054

# Analisis Kuis 1

## MERGE SORT

### Penjelasan Algoritma
Merge Sort adalah algoritma pengurutan berbasis divide-and-conquer yang membagi array menjadi dua bagian, mengurutkan masing-masing bagian secara rekursif, lalu menggabungkan hasilnya menjadi array yang terurut.

### Analisis Kompleksitas Waktu
- **Worst Case**: O(n log n) - Terjadi pada semua kasus karena proses pembagian dan penggabungan selalu konsisten.
- **Best Case**: O(n log n) - Sama seperti kasus terburuk.
- **Average Case**: O(n log n) - Sama seperti kasus terbaik dan terburuk.

## QUICK SORT

### Penjelasan Algoritma
Quick Sort adalah algoritma pengurutan berbasis divide-and-conquer yang memilih elemen sebagai pivot, lalu mempartisi array ke dalam tiga bagian: elemen yang lebih kecil, elemen yang sama, dan elemen yang lebih besar dari pivot.

### Analisis Kompleksitas Waktu
- **Worst Case**: O(n²) - Terjadi ketika pivot selalu elemen terkecil atau terbesar.
- **Best Case**: O(n log n) - Terjadi ketika pivot adalah elemen median.
- **Average Case**: O(n log n) - Rata-rata pivot membagi array dengan proporsi yang seimbang.

# Analisis Kuis 2

## Analisis Algoritma Penguruta

Proyek ini mengimplementasikan dan menganalisis dua algoritma pengurutan:  
1. Pendekatan Naif (Bubble Sort)  
2. Pendekatan Divide-and-Conquer (Merge Sort)  

## Analisis Best Case

### 1. Bubble Sort (Pendekatan Naif)

Pada kasus terbaik, array sudah terurut, sehingga tidak ada pertukaran yang terjadi. Loop akan berhenti lebih cepat karena flag `swapped` tetap `False`.

- **Jumlah Perbandingan:** Hanya perlu `n-1` perbandingan (49 kali untuk array dengan 50 elemen).
- **Jumlah Pertukaran:** Tidak ada pertukaran (`swaps = 0`).

#### Kompleksitas:
- **Best Case Time Complexity:** O(n)
- **Space Complexity:** O(1)

### 2. Merge Sort (Conquer)

Pada kasus terbaik, jumlah perbandingan tetap sama seperti pada kasus umum karena pembagian dan penggabungan tidak tergantung pada pengurutan array.

- **Jumlah Perbandingan:** Tetap `n log(n)` untuk 50 elemen.
- **Jumlah Pertukaran:** Tidak relevan karena hanya terjadi penggabungan.

#### Kompleksitas:
- **Best Case Time Complexity:** O(n log(n))
- **Space Complexity:** O(n) (karena membutuhkan array tambahan untuk penggabungan)
