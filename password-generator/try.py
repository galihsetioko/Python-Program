import random
import string

def generate_password(length=12):
    # Buat karakter yang dapat digunakan dalam kata sandi (huruf besar, huruf kecil, dan angka)
    characters = string.ascii_letters + string.digits + string.octdigits
    
    # Hasilkan kata sandi acak dengan panjang tertentu
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Menggunakan fungsi untuk menghasilkan kata sandi
password = generate_password()
print("Kata Sandi Acak Anda:", password)
