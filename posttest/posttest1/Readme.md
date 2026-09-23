# SWEET PASTRY SHOP – PROGRAM OOP PYTHON

## 1. Deskripsi Program

**Sweet Pastry Shop** merupakan program pengelolaan produk pastry dan transaksi pemesanan yang dibuat menggunakan bahasa pemrograman **Python** dengan pendekatan **Object-Oriented Programming (OOP)**.

Program ini dibuat untuk menerapkan materi pemrograman berorientasi objek yang telah dipelajari, yaitu:

1. Class dan Object
2. Atribut dan Method
3. Encapsulation dan Property
4. Inheritance
5. Polymorphism
6. Abstraction
7. CRUD (Create, Read, Update, Delete)

Program dapat digunakan untuk mengelola data produk pastry, produk yang sedang mendapatkan diskon, serta transaksi pemesanan pelanggan.

---

# 2. Tujuan Program

Program ini bertujuan untuk:

* Menyimpan dan mengelola data produk pastry.
* Menampilkan daftar produk yang tersedia.
* Menambahkan produk baru.
* Mengubah informasi produk.
* Menghapus produk dari daftar inventaris.
* Mengelola produk yang memiliki diskon.
* Membuat transaksi pemesanan pelanggan.
* Menghitung total harga pembelian.
* Memproses pembayaran pelanggan.
* Menerapkan konsep OOP dalam sebuah program sederhana.

---

# 3. Fitur Program

Program memiliki beberapa fitur utama sebagai berikut.

### A. CRUD Produk

Program menyediakan operasi CRUD untuk data produk pastry.

#### Create

Digunakan untuk menambahkan produk pastry baru ke dalam daftar inventaris.

Data yang dimasukkan:

* Kode produk
* Nama produk
* Harga
* Stok

#### Read

Digunakan untuk menampilkan seluruh produk pastry yang tersimpan.

#### Update

Digunakan untuk mengubah informasi produk yang sudah tersedia, seperti:

* Nama produk
* Harga
* Stok

#### Delete

Digunakan untuk menghapus produk berdasarkan kode produk.

---

### B. Produk Diskon

Program memiliki class `ProdukDiskon` yang digunakan untuk menyimpan produk yang sedang mendapatkan promo.

Data tambahan yang dimiliki:

* Persentase diskon
* Masa berlaku promo

Program kemudian dapat menghitung harga akhir produk setelah mendapatkan diskon.

---

### C. Transaksi Pemesanan

Class `TransaksiPemesanan` digunakan untuk mengelola proses pemesanan pelanggan.

Fitur transaksi meliputi:

* Menyimpan nomor transaksi.
* Menyimpan nama pelanggan.
* Menambahkan produk ke transaksi.
* Mengurangi stok produk.
* Menghitung total harga.
* Menambahkan biaya layanan.
* Memproses pembayaran.
* Menghitung kembalian.
* Menampilkan detail transaksi.

---

# 4. Struktur Class

Program memiliki tiga class utama yang sesuai dengan tema, yaitu:

```text
ProdukPastry
      │
      ├── ProdukBiasa
      │
      └── ProdukDiskon

TransaksiPemesanan
```

`ProdukPastry` menjadi superclass atau class induk untuk produk pastry.

`ProdukBiasa` dan `ProdukDiskon` merupakan class turunan dari `ProdukPastry`.

Sedangkan `TransaksiPemesanan` merupakan class yang digunakan untuk mengelola transaksi pembelian.

---

# 5. Penjelasan Class

## 5.1 Class ProdukPastry

Class `ProdukPastry` merupakan class dasar yang menyimpan informasi umum mengenai produk pastry.

Atribut yang dimiliki:

```python
nama_toko
total_produk
kategori_toko
```

Ketiga atribut tersebut merupakan **atribut kelas** karena nilainya digunakan bersama oleh objek yang dibuat dari class.

Atribut instance yang digunakan:

```python
self.kode_produk
self.nama_produk
self.harga
self.__stok
```

`kode_produk`, `nama_produk`, dan `harga` merupakan atribut public.

Sedangkan `__stok` merupakan atribut private sehingga tidak dapat diakses secara langsung dari luar class.

### Method pada ProdukPastry

Beberapa method yang terdapat pada class ini yaitu:

* `tampilkan_info()`
* `kurangi_stok()`
* `tambah_total_produk()`
* `dari_dictionary()`
* `validasi_harga()`
* `hitung_harga_akhir()`

Class ini juga menggunakan `ABC` dan `abstractmethod` untuk menerapkan konsep abstraction.

---

# 6. Class ProdukBiasa

`ProdukBiasa` merupakan class turunan dari `ProdukPastry`.

Class ini digunakan untuk produk pastry yang tidak mendapatkan diskon.

Class ini mengimplementasikan method:

```python
hitung_harga_akhir()
```

Pada produk biasa, harga akhir sama dengan harga awal produk.

Contohnya:

```text
Harga = Rp15.000
Harga akhir = Rp15.000
```

Class ini digunakan sebagai objek produk biasa pada program.

---

# 7. Class ProdukDiskon

`ProdukDiskon` merupakan class turunan dari `ProdukPastry`.

Class ini digunakan untuk produk yang sedang mendapatkan promo.

Atribut tambahan:

```python
persentase_diskon
masa_berlaku
```

Method utama:

```python
hitung_harga_akhir()
```

Method tersebut digunakan untuk menghitung harga setelah diskon.

Contoh:

```text
Harga awal       = Rp20.000
Diskon           = 20%
Harga setelah    = Rp16.000
```

Class `ProdukDiskon` juga melakukan overriding terhadap method `tampilkan_info()` dan `hitung_harga_akhir()`.

---

# 8. Class TransaksiPemesanan

Class `TransaksiPemesanan` digunakan untuk mengelola proses pembelian oleh pelanggan.

Atribut kelas:

```python
nama_toko
biaya_layanan
total_transaksi
```

Atribut instance:

```python
nomor_transaksi
nama_pelanggan
daftar_produk
__status_pembayaran
```

`__status_pembayaran` merupakan atribut private.

Getter dan setter digunakan untuk mengakses atribut tersebut.

Method yang terdapat pada class ini:

* `tambah_produk()`
* `hitung_total()`
* `proses_pembayaran()`
* `tampilkan_transaksi()`
* `ubah_biaya_layanan()`
* `validasi_nama_pelanggan()`

---

# 9. Penerapan Pilar-Pilar PBO

## 9.1 Encapsulation

Encapsulation diterapkan dengan menyembunyikan data penting menggunakan atribut private.

Contohnya:

```python
self.__stok
```

dan:

```python
self.__status_pembayaran
```

Data tersebut tidak diakses secara langsung dari luar class.

Akses terhadap data private dilakukan menggunakan property.

Contohnya:

```python
@property
def stok(self):
    return self.__stok
```

---

## 9.2 Inheritance

Inheritance digunakan agar class turunan dapat menggunakan atribut dan method dari class induknya.

Contohnya:

```python
class ProdukDiskon(ProdukPastry):
```

Artinya `ProdukDiskon` mewarisi atribut dan method dari `ProdukPastry`.

Class `ProdukBiasa` juga menggunakan inheritance:

```python
class ProdukBiasa(ProdukPastry):
```

Dengan inheritance, kode yang sudah terdapat pada `ProdukPastry` dapat digunakan kembali oleh class turunannya.

---

## 9.3 Polymorphism

Polymorphism diterapkan melalui method:

```python
hitung_harga_akhir()
```

Pada `ProdukBiasa`, method tersebut mengembalikan harga normal:

```python
def hitung_harga_akhir(self):
    return self.harga
```

Sedangkan pada `ProdukDiskon`, method yang sama digunakan untuk menghitung harga setelah diskon:

```python
def hitung_harga_akhir(self):
    harga_diskon = self.harga * (
        1 - self.persentase_diskon / 100
    )
    return harga_diskon
```

Walaupun nama method sama, perilakunya berbeda tergantung objek yang digunakan.

---

## 9.4 Abstraction

Abstraction diterapkan menggunakan:

```python
from abc import ABC, abstractmethod
```

Class `ProdukPastry` dibuat sebagai abstract class:

```python
class ProdukPastry(ABC):
```

Kemudian terdapat abstract method:

```python
@abstractmethod
def hitung_harga_akhir(self):
    pass
```

Method tersebut wajib diimplementasikan oleh class turunannya.

Dengan abstraction, class induk hanya menentukan fungsi yang harus tersedia tanpa menentukan secara detail bagaimana fungsi tersebut dilakukan.

---

# 10. Atribut Kelas

Program memiliki beberapa atribut kelas.

### Pada `ProdukPastry`

```python
nama_toko = "Sweet Pastry"
total_produk = 0
kategori_toko = "Pastry & Bakery"
```

Atribut tersebut digunakan bersama oleh objek dari class yang bersangkutan.

### Pada `TransaksiPemesanan`

```python
nama_toko = "Sweet Pastry"
biaya_layanan = 2000
total_transaksi = 0
```

Atribut tersebut digunakan untuk menyimpan konfigurasi dan informasi umum transaksi.

---

# 11. Atribut Instance

Atribut instance dibuat di dalam method `__init__()` menggunakan `self`.

Contohnya:

```python
self.kode_produk = kode_produk
self.nama_produk = nama_produk
self.harga = harga
self.__stok = stok
```

Nilai atribut instance dapat berbeda untuk setiap objek.

Contohnya:

```python
produk1 = ProdukBiasa(
    "P001",
    "Croissant",
    15000,
    20
)

produk2 = ProdukBiasa(
    "P002",
    "Donat Cokelat",
    12000,
    15
)
```

Walaupun berasal dari class yang sama, setiap objek memiliki data yang berbeda.

---

# 12. Getter dan Setter

Program menggunakan decorator `@property` sebagai getter.

Contohnya:

```python
@property
def stok(self):
    return self.__stok
```

Getter digunakan untuk mengambil nilai dari atribut private.

Setter digunakan untuk mengubah nilai atribut private.

```python
@stok.setter
def stok(self, nilai):
    if not isinstance(nilai, int):
        print("Stok harus berupa bilangan bulat!")
        return

    if nilai < 0:
        print("Stok tidak boleh negatif!")
        return

    self.__stok = nilai
```

Setter juga memiliki validasi sehingga data yang tidak sesuai tidak akan diterima.

---

# 13. Method yang Digunakan

## 13.1 Instance Method

Instance method merupakan method yang menggunakan parameter `self`.

Contoh:

```python
def tampilkan_info(self):
```

Method ini digunakan untuk menampilkan informasi produk berdasarkan data objek.

Contoh lainnya:

```python
def tambah_produk(self, produk, jumlah):
```

Method ini digunakan untuk menambahkan produk ke dalam transaksi.

---

## 13.2 Class Method

Class method menggunakan decorator:

```python
@classmethod
```

dan menerima parameter `cls`.

Contoh:

```python
@classmethod
def ubah_biaya_layanan(cls, biaya):
```

Method tersebut digunakan untuk mengubah biaya layanan yang merupakan atribut kelas.

Program juga memiliki factory method:

```python
@classmethod
def dari_dictionary(cls, data):
```

Method tersebut dapat membuat objek berdasarkan data dictionary.

---

## 13.3 Static Method

Static method menggunakan decorator:

```python
@staticmethod
```

Static method tidak membutuhkan `self` maupun `cls`.

Contohnya:

```python
@staticmethod
def validasi_harga(harga):
    return isinstance(harga, (int, float)) and harga > 0
```

Method tersebut digunakan untuk melakukan validasi harga.

Contoh lainnya:

```python
@staticmethod
def validasi_diskon(diskon):
    return 0 <= diskon <= 100
```

Method tersebut digunakan untuk memastikan nilai diskon berada pada rentang 0 sampai 100 persen.

---

# 14. Panduan Menjalankan Program

## 14.1 Persiapan

Pastikan Python sudah terinstal pada komputer.

Untuk mengecek instalasi Python, jalankan:

```bash
python --version
```

atau:

```bash
python3 --version
```

---

## 14.2 Menjalankan Program

Simpan program dengan nama:

```text
main.py
```

Kemudian buka terminal pada folder tempat file berada.

Jalankan dengan:

```bash
python main.py
```

Jika menggunakan Linux atau beberapa konfigurasi lainnya, dapat menggunakan:

```bash
python3 main.py
```

---

# 15. Panduan Pengujian Program

Program sudah memiliki bagian pengujian pada bagian bawah `main.py`.

## Pengujian 1 – Produk Pastry

Program membuat minimal dua objek produk biasa:

```python
produk1
produk2
```

Contoh data:

```text
P001 - Croissant
P002 - Donat Cokelat
```

Kemudian informasi produk ditampilkan menggunakan:

```python
produk1.tampilkan_info()
produk2.tampilkan_info()
```

Pengujian ini menunjukkan penggunaan **object dan instance method**.

---

## Pengujian 2 – Produk Diskon

Program membuat dua objek produk diskon:

```python
diskon1
diskon2
```

Contoh:

```text
D001 - Cinnamon Roll
D002 - Strawberry Danish
```

Informasi produk dan harga setelah diskon kemudian ditampilkan.

Pengujian ini menunjukkan penerapan **inheritance dan polymorphism**.

---

## Pengujian 3 – Class Method

Program menguji class method untuk mengubah biaya layanan:

```python
TransaksiPemesanan.ubah_biaya_layanan(3000)
```

Setelah method dijalankan, biaya layanan berubah menjadi:

```text
Rp3.000
```

Pengujian ini membuktikan penggunaan `@classmethod`.

---

## Pengujian 4 – Static Method

Program menguji validasi harga:

```python
ProdukPastry.validasi_harga(15000)
```

Hasil:

```text
True
```

Kemudian diuji dengan:

```python
ProdukPastry.validasi_harga(0)
```

Hasil:

```text
False
```

Pengujian ini membuktikan penggunaan `@staticmethod`.

---

## Pengujian 5 – Setter dengan Data Valid

Program mengubah stok menggunakan setter:

```python
produk1.stok = 25
```

Karena `25` merupakan bilangan bulat dan tidak negatif, perubahan diterima.

Hasil:

```text
Stok berhasil diperbarui.
```

---

## Pengujian 6 – Setter dengan Data Tidak Valid

Program kemudian mencoba:

```python
produk1.stok = -10
```

Karena stok tidak boleh negatif, perubahan ditolak.

Hasil:

```text
Stok tidak boleh negatif!
```

Stok tetap menggunakan nilai sebelumnya.

Pengujian ini membuktikan bahwa validasi pada setter berjalan dengan baik.

---

## Pengujian 7 – Transaksi

Program membuat dua objek transaksi:

```python
transaksi1
transaksi2
```

Contohnya:

```text
TRX001 - Andi
TRX002 - Siti
```

Produk kemudian dimasukkan ke dalam transaksi menggunakan:

```python
transaksi1.tambah_produk(produk1, 2)
```

Program akan mengurangi stok produk secara otomatis.

---

## Pengujian 8 – Perhitungan Total

Program menghitung total transaksi menggunakan:

```python
transaksi1.hitung_total()
```

Total terdiri dari:

```text
Harga produk
+ Biaya layanan
= Total pembayaran
```

Untuk produk diskon, harga yang digunakan adalah harga setelah diskon.

---

## Pengujian 9 – Pembayaran

Pembayaran dilakukan menggunakan:

```python
transaksi1.proses_pembayaran(100000)
```

Program akan:

1. Menghitung total pembayaran.
2. Mengecek apakah uang mencukupi.
3. Mengubah status menjadi `Sudah Dibayar`.
4. Menghitung kembalian.

---

## Pengujian 10 – Factory Method

Program juga menguji factory method dengan dictionary:

```python
data_produk = {
    "kode": "P003",
    "nama": "Muffin",
    "harga": 18000,
    "stok": 12
}
```

Kemudian dibuat objek menggunakan:

```python
produk3 = ProdukPastry.dari_dictionary(data_produk)
```

Pengujian ini menunjukkan penggunaan `@classmethod` sebagai factory method.

---

# 16. Alur Program

Secara umum, alur program adalah:

```text
Mulai
  |
  v
Membuat objek produk
  |
  v
Membuat objek produk diskon
  |
  v
Pengujian method dan property
  |
  v
Membuat transaksi
  |
  v
Menambahkan produk
  |
  v
Menghitung total
  |
  v
Melakukan pembayaran
  |
  v
Masuk ke Menu CRUD
  |
  +------> Create
  |
  +------> Read
  |
  +------> Update
  |
  +------> Delete
  |
  +------> Keluar
  |
  v
Selesai
```

---

# 17. Contoh Menu CRUD

Setelah pengujian awal selesai, program akan menampilkan menu:

```text
======================================
             MENU CRUD
======================================
1. Create - Tambah Produk
2. Read   - Tampilkan Produk
3. Update - Ubah Produk
4. Delete - Hapus Produk
5. Keluar
======================================
Pilih menu:
```

Pengguna dapat memilih operasi yang ingin dilakukan.

---

# 18. Struktur File Repository

Struktur repository GitHub yang digunakan:

```text
sweet-pastry-oop/
│
├── main.py
│
└── README.md
```