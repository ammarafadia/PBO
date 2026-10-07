# Pengembangan PBO Sweet Pastry Shop

## Deskripsi

Bagian ini merupakan pengembangan dari program **Sweet Pastry Shop** yang sudah dibuat sebelumnya. Pengembangan dilakukan untuk memenuhi kebutuhan tugas tambahan mengenai konsep **Inheritance** serta hubungan antar-class dalam **UML**, yaitu **Association, Aggregation, dan Composition**.

Pengembangan ini ditambahkan tanpa mengubah struktur program utama yang sudah ada.

## Tujuan

Pengembangan program bertujuan untuk menerapkan:

* Inheritance
* Superclass dan subclass
* `super().__init__()`
* Protected attribute
* Method overriding
* Multiple inheritance
* Association
* Aggregation
* Composition

## 1. Inheritance

Inheritance digunakan agar sebuah class dapat mewarisi atribut dan method dari class lain.

Struktur inheritance yang digunakan:

```text
ProdukPastryDasar
       |
       +------ ProdukKue
       |
       +------ ProdukRoti
```

### Superclass

```python
class ProdukPastryDasar:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def tampilkan_info(self):
        return f"{self._nama} - Rp{self._harga}"
```

`ProdukPastryDasar` merupakan superclass yang memiliki:

* `_nama`
* `_harga`
* `tampilkan_info()`

Atribut `_nama` menggunakan satu underscore sehingga bersifat **protected** dan dapat digunakan oleh subclass.

### Subclass ProdukKue

```python
class ProdukKue(ProdukPastryDasar):
    def __init__(self, nama, harga, rasa):
        super().__init__(nama, harga)
        self.rasa = rasa
```

`ProdukKue` mewarisi `ProdukPastryDasar`.

Subclass ini memiliki atribut khusus:

```text
rasa
```

Constructor superclass dipanggil menggunakan:

```python
super().__init__(nama, harga)
```

Method `tampilkan_info()` juga dioverride untuk menampilkan informasi khusus produk kue.

### Subclass ProdukRoti

```python
class ProdukRoti(ProdukPastryDasar):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran
```

`ProdukRoti` juga mewarisi `ProdukPastryDasar`.

Atribut khusus yang dimiliki:

```text
ukuran
```

Subclass ini juga menggunakan:

```python
super().__init__(nama, harga)
```

dan melakukan overriding terhadap method `tampilkan_info()`.

## 2. Protected Attribute

Superclass menggunakan atribut:

```python
self._nama
self._harga
```

Atribut tersebut menggunakan satu underscore sehingga digunakan sebagai atribut protected.

Subclass dapat mengakses atribut tersebut secara langsung.

Contohnya:

```python
return f"Kue: {self._nama} | Harga: Rp{self._harga} | Rasa: {self.rasa}"
```

Dengan demikian, subclass `ProdukKue` dan `ProdukRoti` dapat menggunakan `_nama` dan `_harga` yang berasal dari superclass.

## 3. Method Overriding

Method `tampilkan_info()` pada superclass:

```python
def tampilkan_info(self):
    return f"{self._nama} - Rp{self._harga}"
```

Kemudian method tersebut dibuat ulang pada subclass.

Pada `ProdukKue`:

```python
def tampilkan_info(self):
    return f"Kue: {self._nama} | Harga: Rp{self._harga} | Rasa: {self.rasa}"
```

Pada `ProdukRoti`:

```python
def tampilkan_info(self):
    return f"Roti: {self._nama} | Harga: Rp{self._harga} | Ukuran: {self.ukuran}"
```

Hal ini menunjukkan penerapan **method overriding**, karena subclass memberikan implementasi sendiri terhadap method yang berasal dari superclass.

## 4. Multiple Inheritance

Program juga memiliki contoh multiple inheritance melalui class `ProdukPromo`.

Strukturnya:

```text
ProdukPastryDasar
       |
   ProdukKue
       |
       +------ ProdukPromo
                ^
                |
          PromoPastry
```

`ProdukPromo` memperoleh kemampuan dari:

```python
class ProdukPromo(ProdukKue, PromoPastry):
```

Dengan demikian, `ProdukPromo` dapat menggunakan fitur dari `ProdukKue` dan `PromoPastry`.

Class `PromoPastry` memiliki atribut:

```python
self.diskon
```

serta method:

```python
hitung_diskon()
```

Produk promo kemudian dapat menghitung harga setelah diskon.

## 5. Association

Association merupakan hubungan antar-class yang bersifat menggunakan class lain tanpa harus memiliki atau mengelolanya secara langsung.

Pada program digunakan class:

```python
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

    def melakukan_pemesanan(self, transaksi):
        print(f"{self.nama} melakukan pemesanan.")
        transaksi.tampilkan_transaksi()
```

`Pelanggan` berhubungan dengan `TransaksiPemesanan` melalui parameter:

```python
transaksi
```

Hubungannya:

```text
Pelanggan -------- TransaksiPemesanan
        Association
```

Pelanggan hanya menggunakan objek transaksi ketika melakukan pemesanan.

## 6. Aggregation

Aggregation merupakan hubungan ketika sebuah class memiliki atau mengelola objek dari class lain, tetapi objek tersebut tetap dapat berdiri sendiri.

Pada program digunakan:

```python
class TokoPastry:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)
```

Produk dibuat di luar `TokoPastry`, kemudian dimasukkan ke dalam toko:

```python
toko1.tambah_produk(kue1)
toko1.tambah_produk(roti1)
```

Hubungannya:

```text
TokoPastry ◇-------- Produk
          Aggregation
```

Produk tetap dapat digunakan walaupun objek `TokoPastry` dihapus.

## 7. Composition

Composition merupakan hubungan yang lebih kuat dibandingkan aggregation. Objek bagian dibuat dan dikelola oleh objek pemiliknya.

Pada program digunakan:

```python
class ResepPastry:
    def __init__(self, nama_resep):
        self.nama_resep = nama_resep
        self.daftar_bahan = []

    def tambah_bahan(self, nama, jumlah):
        bahan = BahanPastry(nama, jumlah)
        self.daftar_bahan.append(bahan)
```

Objek `BahanPastry` dibuat langsung di dalam method `tambah_bahan()` milik `ResepPastry`.

Hubungannya:

```text
ResepPastry ◆-------- BahanPastry
           Composition
```

Artinya `ResepPastry` menjadi pemilik dari bahan-bahan yang digunakan dalam resep tersebut.

## 8. Class yang Ditambahkan

| Class               | Fungsi                       |
| ------------------- | ---------------------------- |
| `ProdukPastryDasar` | Superclass produk tambahan   |
| `ProdukKue`         | Subclass untuk produk kue    |
| `ProdukRoti`        | Subclass untuk produk roti   |
| `PromoPastry`       | Menyediakan fitur diskon     |
| `ProdukPromo`       | Produk dengan fitur promo    |
| `BahanPastry`       | Menyimpan data bahan         |
| `ResepPastry`       | Mengelola bahan dalam resep  |
| `TokoPastry`        | Mengelola produk             |
| `Pelanggan`         | Berhubungan dengan transaksi |

## 9. Contoh Penggunaan

### Produk Kue

```python
kue1 = ProdukKue(
    "Chocolate Cake",
    50000,
    "Cokelat"
)

print(kue1.tampilkan_info())
```

Output:

```text
Kue: Chocolate Cake | Harga: Rp50000 | Rasa: Cokelat
```

### Produk Roti

```python
roti1 = ProdukRoti(
    "Croissant",
    25000,
    "Original"
)

print(roti1.tampilkan_info())
```

Output:

```text
Roti: Croissant | Harga: Rp25000 | Ukuran: Original
```

### Produk Promo

```python
promo1 = ProdukPromo(
    "Strawberry Cake",
    60000,
    "Stroberi",
    10
)

print(promo1.tampilkan_info())
```

### Resep

```python
resep1 = ResepPastry("Chocolate Cake")

resep1.tambah_bahan(
    "Tepung",
    "200 gram"
)

resep1.tambah_bahan(
    "Cokelat",
    "100 gram"
)

resep1.tampilkan_resep()
```

### Toko

```python
toko1 = TokoPastry("Sweet Pastry Shop")

toko1.tambah_produk(kue1)
toko1.tambah_produk(roti1)

toko1.tampilkan_produk()
```

### Pelanggan

```python
pelanggan1 = Pelanggan("Kinn")

pelanggan1.melakukan_pemesanan(
    transaksi1
)
```

## 10. Kesimpulan

Pengembangan program Sweet Pastry Shop menerapkan beberapa konsep penting dalam pemrograman berorientasi objek. Inheritance digunakan melalui `ProdukPastryDasar`, `ProdukKue`, dan `ProdukRoti`. Setiap subclass memiliki atribut khusus, menggunakan `super().__init__()`, dan melakukan method overriding.

Selain inheritance, hubungan antar-class juga diterapkan melalui Association pada `Pelanggan` dan `TransaksiPemesanan`, Aggregation pada `TokoPastry` dan produk, serta Composition pada `ResepPastry` dan `BahanPastry`.

Dengan tambahan tersebut, program tidak hanya memiliki fungsi CRUD, tetapi juga menunjukkan penerapan konsep hubungan antar-object dan pewarisan dalam PBO.
