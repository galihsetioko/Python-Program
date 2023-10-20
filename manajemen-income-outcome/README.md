Ini adalah program untuk menyimpan laporan keuangan sederhana dalam format json
program ini menggunakan Command Line Interface untuk menerima input dari pengguna.

Cara menggunakan : 

filename.py -f [filename.json] --income [20000] --description ["Description Here"]

-f , --filename         Memberikan input lokasi file json
-i , --income           Memberi tahu program untuk memasukan data ke dalam dictionary "income"
-o , --outcome          Member tahu program untuk memasukan data ke dalam dictionary "outcome"
-d , --description      Memberi label atau informasi tentang "digunakan untuk membeli apa uangmu"

Gunakan hanya salah satu argument antara --income atau --outcome , jangan gunakan keduanya sekaligus.

Program akan mendeteksi input yang dimasukkan sesuai dengan tanggal ketika dijalankan , ketika kamu menjalankan
program dengan file json yang sama esok hari , maka program otomatis mengganti informasi tanggal pada file json.
Dengan membuat label baru sesuai dengan tanggal terkini.
