#Amirul Maulana
#F55123039

# Data awal
# Analisis: Data ini adalah daftar bilangan yang akan diurutkan menggunakan dua algoritma berbeda: Merge Sort dan Quick Sort.
# Variabel `data_awal` berisi elemen-elemen yang akan menjadi input utama untuk algoritma pengurutan.
data_awal = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


# Fungsi Merge Sort
def pengurutan_merge(array):
    """
    Fungsi ini digunakan untuk mengurutkan array menggunakan algoritma Merge Sort.
    - Parameter `array` adalah daftar elemen yang akan diurutkan.
    - Fungsi ini bersifat rekursif, membagi array menjadi dua bagian hingga hanya terdiri dari satu elemen.
    - Setelah itu, elemen-elemen digabungkan kembali dalam urutan yang benar.
    """

    if len(array) > 1:
        # Menentukan titik tengah array untuk membagi array menjadi dua bagian.
        titik_tengah = len(array) // 2
        bagian_kiri = array[:titik_tengah]  # Bagian kiri array.
        bagian_kanan = array[titik_tengah:]  # Bagian kanan array.

        # Rekursi untuk mengurutkan bagian kiri dan kanan.
        # Fungsi `pengurutan_merge` dipanggil kembali untuk setiap sub-array.
        pengurutan_merge(bagian_kiri)
        pengurutan_merge(bagian_kanan)

        # Inisialisasi indeks untuk menggabungkan dua bagian array.
        indeks_kiri = indeks_kanan = indeks_gabung = 0

        # Menggabungkan elemen bagian kiri dan kanan.
        while indeks_kiri < len(bagian_kiri) and indeks_kanan < len(bagian_kanan):
            if bagian_kiri[indeks_kiri] < bagian_kanan[indeks_kanan]:
                array[indeks_gabung] = bagian_kiri[indeks_kiri]
                indeks_kiri += 1
            else:
                array[indeks_gabung] = bagian_kanan[indeks_kanan]
                indeks_kanan += 1
            indeks_gabung += 1

        # Menambahkan elemen yang tersisa dari bagian kiri.
        while indeks_kiri < len(bagian_kiri):
            array[indeks_gabung] = bagian_kiri[indeks_kiri]
            indeks_kiri += 1
            indeks_gabung += 1

        # Menambahkan elemen yang tersisa dari bagian kanan.
        while indeks_kanan < len(bagian_kanan):
            array[indeks_gabung] = bagian_kanan[indeks_kanan]
            indeks_kanan += 1
            indeks_gabung += 1


# Eksekusi Merge Sort
# Penjelasan: Variabel `data_urut_merge` adalah salinan dari `data_awal` untuk menjaga data asli tetap utuh.
# Fungsi `pengurutan_merge` dipanggil untuk mengurutkan elemen dalam `data_urut_merge`.
data_urut_merge = data_awal.copy()
pengurutan_merge(data_urut_merge)
print("Hasil Pengurutan Merge Sort:", data_urut_merge)
# Analisis: Merge Sort membagi array menjadi beberapa sub-array kecil (divide),
# mengurutkan setiap sub-array, dan kemudian menggabungkannya menjadi array terurut (conquer).


# Fungsi Quick Sort
def pengurutan_cepat(array):
    """
    Fungsi ini digunakan untuk mengurutkan array menggunakan algoritma Quick Sort.
    - Parameter `array` adalah daftar elemen yang akan diurutkan.
    - Fungsi ini menggunakan elemen pivot untuk membagi array menjadi tiga bagian:
      elemen lebih kecil, elemen sama, dan elemen lebih besar.
    - Fungsi ini memanggil dirinya sendiri secara rekursif untuk bagian lebih kecil dan lebih besar.
    """

    if len(array) <= 1:
        # Jika array hanya memiliki satu elemen atau kosong, langsung dikembalikan.
        return array

    # Memilih elemen pivot (elemen tengah array).
    pivot = array[len(array) // 2]

    # Membagi array menjadi tiga bagian berdasarkan nilai pivot.
    lebih_kecil = [x for x in array if x < pivot]  # Elemen yang lebih kecil dari pivot.
    sama_dengan = [x for x in array if x == pivot]  # Elemen yang sama dengan pivot.
    lebih_besar = [x for x in array if x > pivot]  # Elemen yang lebih besar dari pivot.

    # Menggabungkan hasil rekursi pada bagian lebih kecil, elemen sama, dan bagian lebih besar.
    return pengurutan_cepat(lebih_kecil) + sama_dengan + pengurutan_cepat(lebih_besar)


# Eksekusi Quick Sort
# Penjelasan: Fungsi `pengurutan_cepat` dipanggil dengan parameter `data_awal` untuk menghasilkan array terurut.
# Hasil pengurutan disimpan dalam variabel `data_urut_cepat`.
data_urut_cepat = pengurutan_cepat(data_awal)
print("Hasil Pengurutan Quick Sort:", data_urut_cepat)
# Analisis: Quick Sort bekerja dengan memilih pivot dan membagi array.
# Algoritma ini lebih efisien dibanding Merge Sort pada sebagian besar kasus,
# namun kinerjanya bisa menurun jika data sudah terurut karena kompleksitas waktu terburuknya adalah O(n^2).
