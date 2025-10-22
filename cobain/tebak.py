import random
angka_acak = random.randint(1, 100)
tebakan = 0
while True:
    tebakan = int(input("Tebak angka antara 1 sampai 100: "))
    if tebakan < angka_acak:
        print("Terlalu rendah! Ayo coba lagi.")
    elif tebakan > angka_acak:
        print("Terlalu tinggi! Ayo coba lagi.")
    else:
        print("Selamat! Tebakan Anda benar>)")
        break