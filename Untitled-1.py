def login():
    username_benar = "riyadi"
    password_benar = "074"
    percobaan_username = 0
    percobaan_password = 0
    max_percobaan = 3

    while percobaan_username < max_percobaan:
        username_input = input("Masukkan username: ")
        if username_input == username_benar:
            break
        else:
            percobaan_username += 1
            print(f"Username salah! Anda memiliki {max_percobaan - percobaan_username} percobaan lagi.")
    else:
        print("Anda telah melebihi batas percobaan username. Akses ditolak.")
        return False

    while percobaan_password < max_percobaan:
        password_input = input("Masukkan password: ")
        if password_input == password_benar:
            print("Login berhasil!")
            return True
        else:
            percobaan_password += 1
            print(f"Password salah! Anda memiliki {max_percobaan - percobaan_password} percobaan lagi.")
    else:
        print("Anda telah melebihi batas percobaan password. Akses ditolak.")
        return False

if login():
    print("Selamat datang!")
else:
    print("Akses ditolak.")