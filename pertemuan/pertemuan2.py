# class Nasabah:

#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

# nama = input("Masukkan nama: ")
# saldo = input("Masukkan saldo: ")

# user = Nasabah(nama, saldo)

# print(user.nama)
# print(user.saldo)

# dapa = Nasabah("dapa", 1000000)
# print(dapa.nama)                                  ###Public
# print(dapa.saldo)

# class Karyawan:
#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self._gaji = gaji  # protected, hanya "disarankan" diakses dari dalam

# class Manager(Karyawan):
#     def tampilkan_gaji(self):
#         # subclass tetap bisa mengakses atribut protected milik parent
#         print(f"Gaji {self.nama}: {self._gaji}")

# manager = Manager("Daffa", 12000000)
# manager.tampilkan_gaji()
# print(manager._gaji)

# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.__pemilik = pemilik
#         self.__saldo = saldo  # private

#     @property
#     def saldo(self):
#         return self.__saldo

#     @saldo.setter
#     def saldo(self, saldo_baru):
#         if saldo_baru < 0:
#             print("Saldo tidak boleh negatif!")
#         else:
#             self.__saldo = saldo_baru

# dapa = RekeningBank("dapa", 100)

# print(dapa.saldo)
# dapa.saldo = -5 
# print(dapa.saldo)

class Produk:
    def __init__(self, nama, stok):
        self.__nama = nama
        self.__stok = stok

    @property
    def nama(self):
        return self.__nama

    @property
    def stok(self):
        return self.__stok

    @nama.setter
    def nama(self, nama_baru):
        if not nama_baru:
            print("Nama tidak boleh kosong!") 
        else:
            self.__nama = nama_baru

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print("Stok tidak boleh negatif!")
        else:
            self.__stok = stok_baru

croissant = Produk("Croissant", 10)

print(croissant.stok)
croissant.stok = -5
print(croissant.stok)