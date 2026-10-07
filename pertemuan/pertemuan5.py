# class AkunBank:
#     def __init__(self, nama, saldo):
#         self.nama = nama
#         self.saldo = saldo

#     def hitung_bunga(self):
#         return 0

# class Tabungan(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.02

# class Deposito(AkunBank):
#     def hitung_bunga(self):
#         return self.saldo * 0.06

# daftar_akun = [Tabungan("Budi", 1000000), Deposito("Sari", 5000000)]
# for akun in daftar_akun:
#     print(f"Bunga {akun.nama}: Rp {akun.hitung_bunga():,.2f}")

# class RekeningTabungan:
#     def __init__(self, saldo):
#         self.saldo = saldo

#     def tarik_uang(self, jumlah):
#         if jumlah <= self.saldo:
#             self.saldo -= jumlah
#             print(f"Penarikan sebesar Rp {jumlah} berhasil.")
#             print(f"Sisa saldo: Rp {self.saldo}")
#         else:
#             print("Saldo tidak mencukupi untuk penarikan.")

# def proses_penarikan(rekening, jumlah):
#     rekening.tarik_uang(jumlah)

# tabungan = RekeningTabungan(1000000)
# giro = RekeningTabungan(500000)
# proses_penarikan(tabungan, 200000)
# proses_penarikan(giro, 100000)

from abc import ABC, abstractmethod

class Transaksi(ABC):
    @abstractmethod
    def validasi(self):
        """
        Wajib diimplementasikan oleh kelas turunan untuk melakukan validasi transaksi.
        """
        pass

    @abstractmethod
    def eksekusi(self):
        """
        Wajib diimplementasikan oleh kelas turunan untuk mengeksekusi transaksi.
        """
        pass

class TarikTunai(Transaksi):
    def __init__(self, saldo_akun, nominal):
        self.saldo = saldo_akun
        self.nominal = nominal

    def validasi(self):
        if self.nominal > self.saldo:
            return False
        return True

    def eksekusi(self):
        if self.validasi():
            self.saldo -= self.nominal
            print(f"Tarik tunai berhasil. Sisa saldo: {self.saldo}")
        else:
            print("Saldo tidak cukup!")

class TransferGagal(Transaksi):
    def validasi(self):
        return True

try:
    transaksi_gagal = TransferGagal()
except TypeError as e:
    print(f"Error: {e}")

transaksi_sukses = TarikTunai(1000000, 500000)
transaksi_sukses.eksekusi()  # Output: Tarik tunai berhasil. Sisa saldo: 500000
