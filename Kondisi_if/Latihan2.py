# Program mengurutkan data dari yang terkecil

a = int(input("Bilangan ke-1: "))
b = int(input("Bilangan ke-2: "))
c = int(input("Bilangan ke-3: "))

# Bisa tambah lagi kalau mau, misalnya d = int(input(...))

# Simpan ke list agar mudah diurutkan
bilangan = [a, b, c]

# Urutkan secara ascending (dari kecil ke besar)
bilangan.sort()

print("Urutan bilangan:", bilangan)