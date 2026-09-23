# paradigma oop ditemukan karena semakin banyaknya code yang digunakan, paradigma ini membantu untuk mengelola code.
# tidak perlu mengingat key jika memakai oop
# code lebih terstruktur dan mudah dibaca

# pascalcase
class ProductDetail:
    pass

# Penyimpanan Data Tanpa OOP
product_name = "Keyboard"
product_price = 500000
product_stock = 10
product_category = "Aksesoris"
product_brand= "Logitech"

product1_name = "Keyboard"
product1_price = 500000
product1_stock = 10
product1_category= "Aksesoris"
product1_brand= "Logitech"

product2_name = "Mouse"
product2_price = 300000
product2_stock = 15
product2_category = "Aksesoris"
product2_brand= "Logitech"

# Menggunakan List Dictionary
products = [
    {
        "name": "Keyboard",
        "price": 500000,
        "stock": 10,
        "category": "Aksesoris",
        "brand": "Logitech"
    },
    {
        "name": "Mouse",
        "price": 300000,
        "stock": 15,
        "category": "Aksesoris",
        "brand": "Logitech"
    }
]

products[0]["price"]
products[0]["stock"] = 20

# Function Terpisah dari Data
def tambah_stok(product, jumlah):
    product["stock"] += jumlah

def kurangi_stok(product, jumlah):
    if product["stock"] >= jumlah:
        product["stock"] -= jumlah

def ubah_harga(product, harga_baru):
    product["price"] = harga_baru

# Penggunaan OOP: Pembuatan Class
class Product:
    def __init__(self, name, price, stock, category, brand):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.brand = brand

    def tambah_stok(self, jumlah):
        self.stock += jumlah

    def kurangi_stok(self, jumlah):
        if self.stock >= jumlah:
            self.stock -= jumlah

    def ubah_harga(self, harga_baru):
        self.price = harga_baru

mouse = Product("Mouse", 300000, 15, "Aksesoris", "Logitech")
mouse.tambah_stok(5)
mouse.kurangi_stok(2)
mouse.ubah_harga(280000)

# Struktur Dasar Class
class Laptop:
    # isi dari class Laptop, berupa attribute dan method
    pass

laptop = Laptop()

# Attribute dan Method pada Class
class Laptop:
    brand = "Lenovo"
    price = 8000000
    
    def change_price(self, new_price):
        self.price = new_price

# Penggunaan Constructor dan self
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

    def change_price(self, new_price):
        self.price = new_price
        self.show_info() # memanggil method lain menggunakan self

laptop1 = Laptop("Lenovo", 8000000)
laptop2 = Laptop("Asus", 10000000)

print(laptop1.brand)
print(laptop1.price)
print(laptop2.brand)
print(laptop2.price)

laptop = Laptop("Lenovo", 8000000)
laptop.change_price(7500000)













# # Contoh Atribut Instance
# class Tim:
#     def __init__(self, nama, ceo):
#         self.nama = nama
#         self.ceo = ceo

# rrq = Tim("RRQ Hoshi", "Pak AP")
# evos = Tim("Evos Legends", "Hartman Harris")

# print(rrq.nama) # RRQ Hoshi
# print(evos.nama) # Evos Legends

# rrq.ceo = "Pak AP Manullang"
# print(rrq.ceo) # Pak AP Manullang
# print(evos.ceo) # Hartman Harris


# # Contoh Atribut Kelas
# class Tim:
#     nama_liga = "MPL Indonesia"
#     def __init__(self, nama, ceo):
#         self.nama = nama
#         self.ceo = ceo

# rrq = Tim("RRQ", "Pak AP")
# evos = Tim("Evos Legends", "Hartman Harris")
# print(rrq.nama_liga) # MPL Indonesia
# print(evos.nama_liga) # MPL Indonesia

# Tim.nama_liga = "MPL Indonesia Season 15"
# print(rrq.nama_liga) # MPL Indonesia Season 15
# print(evos.nama_liga) # MPL Indonesia Season 15


# # Gabungan Atribut Instance dan Kelas
# class Tim:
#     nama_liga = "MPL Indonesia"
#     def __init__(self, nama, ceo):
#         self.nama = nama
#         self.ceo = ceo

# rrq = Tim("RRQ Hoshi", "Pak AP")
# evos = Tim("Evos Legends", "Hartman Harris")
# alter_ego = Tim("Alter Ego", "Koh Delwyn")

# print(f"{rrq.nama} (CEO: {rrq.ceo}) Liga: {Tim.nama_liga}\n")
# print(f"{evos.nama} (CEO: {evos.ceo}) Liga: {Tim.nama_liga}\n")
# print(f"{alter_ego.nama} (CEO: {alter_ego.ceo}) Liga: {Tim.nama_liga}\n")

# rrq.ceo = "Pak AP Manullang"
# print(f"{rrq.nama} (CEO: {rrq.ceo}) Liga: {Tim.nama_liga}\n")

# Tim.nama_liga = "MPL Indonesia Season 15"
# print(f"{rrq.nama} (CEO: {rrq.ceo}) Liga: {Tim.nama_liga}\n")
# print(f"{evos.nama} (CEO: {evos.ceo}) Liga: {Tim.nama_liga}\n")
# print(f"{alter_ego.nama} (CEO: {alter_ego.ceo}) Liga: {Tim.nama_liga}\n")


# # Penerapan Instance Method, Class Method, dan Static Method secara keseluruhan
# class Pertandingan:
#     musim_liga = "MPL Indonesia Season 14"
    
#     def __init__(self, tim_a, tim_b):
#         self.tim_a = tim_a
#         self.tim_b = tim_b
#         self.skor_a = 0
#         self.skor_b = 0
#         self.selesai = False

#     def tambah_skor(self, tim, poin=1):
#         if tim == self.tim_a:
#             self.skor_a += poin
#         elif tim == self.tim_b:
#             self.skor_b += poin
#         else:
#             print(f"{tim} tidak terdaftar di pertandingan ini!")

#     def selesaikan(self):
#         self.selesai = True

#     def tampilkan_hasil(self):
#         status = "Selesai" if self.selesai else "Berlangsung"
#         print(f"{self.tim_a} {self.skor_a} - {self.skor_b} {self.tim_b} ({status}, {Pertandingan.musim_liga})")

#     @classmethod
#     def dari_dict(cls, data):
#         return cls(data["tim_a"], data["tim_b"])

#     @classmethod
#     def ganti_musim(cls, musim_baru):
#         cls.musim_liga = musim_baru

#     @staticmethod
#     def validasi_nama_tim(nama_tim):
#         tim_terdaftar = ["RRQ", "Evos Legends", "Alter Ego", "ONIC"]
#         return nama_tim in tim_terdaftar

#     @staticmethod
#     def tentukan_pemenang(tim_a, skor_a, tim_b, skor_b):
#         if skor_a > skor_b:
#             return tim_a
#         elif skor_b > skor_a:
#             return tim_b
#         return "Seri"

# print(Pertandingan.validasi_nama_tim("RRQ"))
# print(Pertandingan.validasi_nama_tim("Team Baru"))

# final = Pertandingan("RRQ", "Evos Legends")
# final.tambah_skor("RRQ", 2)
# final.tambah_skor("Evos Legends", 1)
# final.selesaikan()
# final.tampilkan_hasil()

# data_laga = {"tim_a": "ONIC", "tim_b": "Alter Ego"}
# laga2 = Pertandingan.dari_dict(data_laga)
# laga2.tambah_skor("ONIC", 2)
# laga2.tampilkan_hasil()

# Pertandingan.ganti_musim("MPL Indonesia Season 15")
# final.tampilkan_hasil()
# laga2.tampilkan_hasil()

# pemenang = Pertandingan.tentukan_pemenang("RRQ", final.skor_a, "Evos Legends", final.skor_b)
# print(f"Pemenang: {pemenang}")
