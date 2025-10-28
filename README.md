# STRUKTUR KONDISI

Latihan 1
 Buat program sederhana dengan input 4 buah bilangan, kemudian
 tentukan bilangan terbesar dari kedua bilangan tersebut
 menggunakan statement if.

Alur program

1. Program meminta 4 input bilangan dari pengguna
2. Variable "terbesar" diinisialisaikan dengan nilai a
3. setiap bilangan lain dibandingkan menggunakan if
4. jika ditemukan bilangan yang lebih besar, nilainya menggantikan terbesar.
5. diakhir, hasilnya ditampilkan

Latihan 2
Buat program untuk mengurutkan data berdasarkan input sejumlah data (minimal 3 variable input atau lebih), kemudian tampilkan hasilnya secara berurutan mulai dari data terkecil.

Alur program

1. mulai program
2. minta pengguna memsaukan jumlah data
3. inisisalisasi list kosong untuk menampung data
4. ulangi proses input sejumlah data
5. simpan setiap data ke dalam list
6. setelah semua data masuk, urutkan data dari terkecil ke terbesar
7. tampilakn hasil urutan
8. selesai

# PERULANGAN

Latihan 1
Buat program dengan perulangan bertingkat (nested) for.

Alur program

1. Mulai program
2. Inisialisasi perulangan luar (for i in range(10))
3. Masuk ke perulangan dalam (for j in range(10))
4. Hitung hasil penjumlahan i + j
5. Cetak hasil
   >Nilai i + j dicetak di baris yang sama.
   >Gunakan end="\t" agar hasilnya dipisahkan dengan tab, bukan baris baru.
6. Selesai satu baris
   >Setelah loop j selesai (artinya satu baris penuh tercetak),
    program mengeksekusi print() kosong untuk pindah ke baris baru.
7. Ulangi langkah 3–6
8. Setelah semua perulangan selesai
  >Program berhenti setelah seluruh tabel (10x10) tercetak.
9. Selesai

Latihan 2
Tampilkan n bilangan acak yang lebih kecil dari 0.5. 
nilai n diisi pada saat runtime
anda bisa menggunakan kombinasi while dan for untuk 
menyelesaikannya

1. Mulai
2. Import modul random
3. Input nilai n dari pengguna
4. Inisialisasi count = 0
5. Jalankan loop while count < n
6. Di dalamnya, jalankan loop for i in range(5)
7. Hasilkan bilangan acak bilangan = random.random()
8. Jika bilangan < 0.5, cetak bilangan dan tambahkan count
9. Jika count == n, keluar dari for
10. Ulangi hingga while selesai
11. Selesai
