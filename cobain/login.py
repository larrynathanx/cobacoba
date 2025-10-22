def login():
    username_benar = "LarryNathanx" 
    password_benar = "The1andONLY"
    percobaan_username = 0
    percobaan_password = 0
    max_percobaan = 2

    while percobaan_username < max_percobaan and percobaan_password < max_percobaan:
        username_input = input("Masukkan username Anda: ")
        if username_input == username_benar:
            break
        else:
            percobaan_username += 1
            print(f"Username Anda salah. Anda memiliki {max_percobaan - percobaan_username}")
    else:
        print("Anda telah melebihi batas percobaan username. Akses ditolak")
        return False
    
    while percobaan_password < max_percobaan:
        password_input = input("Masukkan password Anda: ")
        if password_input == password_benar:
            print("Login Berhasil!")
            return True
        else:
            percobaan_password += 1
            print(f"Password Anda salah. Anda memiliki {max_percobaan - percobaan_password} percobaan lagi")
    else:
        print("Anda telah melebihi batas percobaan password. Akses Ditolak")
        return False
        
if login():
        print("Selamat datang")
else:
        print("Akses DITOLAK!")
    
