import random

n = int(input("Masukkan jumlah n: "))  # input jumlah bilangan
count = 0  # penghitung bilangan yang dicetak

while count < n:               # loop sampai jumlah n terpenuhi
    x = random.random()        # menghasilkan bilangan acak 0–1
    if x < 0.5:                # hanya tampilkan jika < 0.5
        print(x)
        count += 1             # hitung bilangan yang dicetak