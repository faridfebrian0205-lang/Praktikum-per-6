import random

# Meminta input dari pengguna
n = int(input("Masukkan jumlah n: "))

count = 0  # penghitung bilangan yang valid

# Gunakan while agar terus mencari bilangan sampai dapat n buah
while count < n:
    # Dalam setiap iterasi while, hasilkan 5 bilangan acak sekaligus menggunakan for
    for i in range(10):
        bilangan = random.random()  # angka acak antara 0.0 - 1.0
        if bilangan < 0.5:
            print(bilangan)
            count += 1
            # Jika sudah cukup n bilangan, hentikan loop
            if count == n:
                break
