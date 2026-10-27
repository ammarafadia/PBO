from abc import ABC, abstractmethod
class ProdukPastry(ABC):
                   
    nama_toko = "Sweet Pastry"
    total_produk = 0
    kategori_toko = "Pastry & Bakery"

    def __init__(self, kode_produk, nama_produk, harga, stok):
                                 
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

                                  
        self.__stok = stok

        ProdukPastry.total_produk += 1

    @property
    def stok(self):
        """Getter untuk mengakses stok private."""
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        """Setter untuk mengubah stok dengan validasi."""
        if not isinstance(nilai, int):
            print("Stok harus berupa bilangan bulat!")
            return

        if nilai < 0:
            print("Stok tidak boleh negatif!")
            return

        self.__stok = nilai
        print("Stok berhasil diperbarui.")

    def tampilkan_info(self):
        print(f"\nKode       : {self.kode_produk}")
        print(f"Nama       : {self.nama_produk}")
        print(f"Harga      : Rp{self.harga:,.0f}")
        print(f"Stok       : {self.stok}")

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0.")
        elif jumlah > self.stok:
            print("Stok tidak mencukupi.")
        else:
            self.stok = self.stok - jumlah
            print(f"Stok {self.nama_produk} berkurang {jumlah}.")

    @classmethod
    def tambah_total_produk(cls, jumlah):
        if jumlah > 0:
            cls.total_produk += jumlah

    @classmethod
    def dari_dictionary(cls, data):
        """
        Factory method untuk membuat objek
        dari sebuah dictionary.
        """
        return ProdukBiasa(
            data["kode"],
            data["nama"],
            data["harga"],
            data["stok"]
        )

    @staticmethod
    def validasi_harga(harga):
        """Utility untuk mengecek apakah harga valid."""
        return isinstance(harga, (int, float)) and harga > 0

    @abstractmethod
    def hitung_harga_akhir(self):
        pass

class ProdukBiasa(ProdukPastry):

    def hitung_harga_akhir(self):
        return self.harga

class ProdukDiskon(ProdukPastry):

    def __init__(
        self,
        kode_produk,
        nama_produk,
        harga,
        stok,
        persentase_diskon,
        masa_berlaku
    ):
        super().__init__(
            kode_produk,
            nama_produk,
            harga,
            stok
        )

                          
        self.persentase_diskon = persentase_diskon
        self.masa_berlaku = masa_berlaku

    def hitung_harga_akhir(self):
        harga_diskon = self.harga * (
            1 - self.persentase_diskon / 100
        )
        return harga_diskon

    def tampilkan_info(self):
        super().tampilkan_info()

        print(f"Diskon     : {self.persentase_diskon}%")
        print(f"Berlaku    : {self.masa_berlaku}")
        print(
            f"Harga Akhir: Rp{self.hitung_harga_akhir():,.0f}"
        )

    @staticmethod
    def validasi_diskon(diskon):
        return 0 <= diskon <= 100

class TransaksiPemesanan:

                   
    nama_toko = "Sweet Pastry"
    biaya_layanan = 2000
    total_transaksi = 0

    def __init__(self, nomor_transaksi, nama_pelanggan):
                          
        self.nomor_transaksi = nomor_transaksi
        self.nama_pelanggan = nama_pelanggan
        self.daftar_produk = []

                         
        self.__status_pembayaran = "Belum Dibayar"

        TransaksiPemesanan.total_transaksi += 1

    @property
    def status_pembayaran(self):
        return self.__status_pembayaran

    @status_pembayaran.setter
    def status_pembayaran(self, status):
        status_valid = [
            "Belum Dibayar",
            "Sudah Dibayar"
        ]

        if status not in status_valid:
            print("Status pembayaran tidak valid!")
            return

        self.__status_pembayaran = status
        print("Status pembayaran berhasil diubah.")

    def tambah_produk(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah produk harus lebih dari 0.")
            return

        if jumlah > produk.stok:
            print("Stok produk tidak mencukupi.")
            return

        self.daftar_produk.append(
            (produk, jumlah)
        )

        produk.kurangi_stok(jumlah)

        print(
            f"{jumlah} {produk.nama_produk} "
            "berhasil ditambahkan ke transaksi."
        )

    def hitung_total(self):
        total = 0

        for produk, jumlah in self.daftar_produk:
            total += produk.hitung_harga_akhir() * jumlah

        total += self.biaya_layanan

        return total

    def proses_pembayaran(self, uang):
        total = self.hitung_total()

        if uang < total:
            print("Uang pembayaran tidak mencukupi.")
            return

        self.status_pembayaran = "Sudah Dibayar"

        kembalian = uang - total

        print(f"Total pembayaran : Rp{total:,.0f}")
        print(f"Uang pelanggan   : Rp{uang:,.0f}")
        print(f"Kembalian        : Rp{kembalian:,.0f}")

    def tampilkan_transaksi(self):
        print("\n======================================")
        print("          DETAIL TRANSAKSI")
        print("======================================")

        print(f"Nomor Transaksi : {self.nomor_transaksi}")
        print(f"Pelanggan       : {self.nama_pelanggan}")

        print("\nDaftar Produk:")

        for produk, jumlah in self.daftar_produk:
            harga = produk.hitung_harga_akhir()

            print(
                f"- {produk.nama_produk} "
                f"x {jumlah} "
                f"= Rp{harga * jumlah:,.0f}"
            )

        print(f"\nBiaya Layanan   : Rp{self.biaya_layanan:,.0f}")
        print(f"Total            : Rp{self.hitung_total():,.0f}")
        print(f"Status Pembayaran: {self.status_pembayaran}")

    @classmethod
    def ubah_biaya_layanan(cls, biaya):
        if biaya < 0:
            print("Biaya layanan tidak boleh negatif.")
            return

        cls.biaya_layanan = biaya
        print("Biaya layanan berhasil diubah.")

    @staticmethod
    def validasi_nama_pelanggan(nama):
        return isinstance(nama, str) and nama.strip() != ""

daftar_produk = []


def create_produk():
    print("\n========== TAMBAH PRODUK ==========")

    kode = input("Kode produk     : ")
    nama = input("Nama produk     : ")

    try:
        harga = float(input("Harga           : "))
        stok = int(input("Stok            : "))
    except ValueError:
        print("Harga atau stok tidak valid!")
        return

    if not ProdukPastry.validasi_harga(harga):
        print("Harga harus lebih dari 0!")
        return

    produk = ProdukBiasa(
        kode,
        nama,
        harga,
        stok
    )

    daftar_produk.append(produk)

    print("Produk berhasil ditambahkan.")


def read_produk():
    print("\n========== DAFTAR PRODUK ==========")

    if len(daftar_produk) == 0:
        print("Belum ada produk.")
        return

    for produk in daftar_produk:
        produk.tampilkan_info()


def update_produk():
    print("\n========== UPDATE PRODUK ==========")

    kode = input("Masukkan kode produk: ")

    for produk in daftar_produk:

        if produk.kode_produk == kode:

            print("Produk ditemukan.")

            nama_baru = input(
                "Nama baru (Enter jika tidak diubah): "
            )

            if nama_baru:
                produk.nama_produk = nama_baru

            try:
                harga_baru = input(
                    "Harga baru (Enter jika tidak diubah): "
                )

                if harga_baru:
                    harga_baru = float(harga_baru)

                    if ProdukPastry.validasi_harga(harga_baru):
                        produk.harga = harga_baru
                    else:
                        print("Harga tidak valid.")

                stok_baru = input(
                    "Stok baru (Enter jika tidak diubah): "
                )

                if stok_baru:
                    produk.stok = int(stok_baru)

            except ValueError:
                print("Input tidak valid.")

            print("Data produk berhasil diperbarui.")
            return

    print("Produk tidak ditemukan.")


def delete_produk():
    print("\n========== HAPUS PRODUK ==========")

    kode = input("Masukkan kode produk: ")

    for produk in daftar_produk:

        if produk.kode_produk == kode:

            daftar_produk.remove(produk)

            print("Produk berhasil dihapus.")
            return

    print("Produk tidak ditemukan.")

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

diskon1 = ProdukDiskon(
    "D001",
    "Cinnamon Roll",
    20000,
    10,
    20,
    "30 September 2026"
)

diskon2 = ProdukDiskon(
    "D002",
    "Strawberry Danish",
    25000,
    8,
    15,
    "30 September 2026"
)

daftar_produk.extend([
    produk1,
    produk2,
    diskon1,
    diskon2
])

if __name__ == "__main__":

    print("==========================================")
    print("       SWEET PASTRY SHOP")
    print("       PROGRAM OOP PYTHON")
    print("==========================================")

    print("\n--- OBJEK PRODUK PASTRY ---")

    produk1.tampilkan_info()
    produk2.tampilkan_info()

    print("\n--- OBJEK PRODUK DISKON ---")

    diskon1.tampilkan_info()
    diskon2.tampilkan_info()

    print("\n--- PENGUJIAN CLASS METHOD ---")

    print(
        "Total produk:",
        ProdukPastry.total_produk
    )

    TransaksiPemesanan.ubah_biaya_layanan(3000)

    print(
        "Biaya layanan baru:",
        TransaksiPemesanan.biaya_layanan
    )

    print("\n--- PENGUJIAN STATIC METHOD ---")

    print(
        "Harga Rp15.000 valid?",
        ProdukPastry.validasi_harga(15000)
    )

    print(
        "Harga Rp0 valid?",
        ProdukPastry.validasi_harga(0)
    )

    print(
        "Diskon 20% valid?",
        ProdukDiskon.validasi_diskon(20)
    )

    print(
        "Nama pelanggan valid?",
        TransaksiPemesanan.validasi_nama_pelanggan(
            "Andi"
        )
    )

    print("\n--- SETTER VALID ---")

    print("Stok sebelum:", produk1.stok)

    produk1.stok = 25

    print("Stok setelah:", produk1.stok)

    print("\n--- SETTER TIDAK VALID ---")

    produk1.stok = -10

    print(
        "Stok setelah input tidak valid:",
        produk1.stok
    )

    print("\n--- OBJEK TRANSAKSI ---")

    transaksi1 = TransaksiPemesanan(
        "TRX001",
        "Andi"
    )

    transaksi2 = TransaksiPemesanan(
        "TRX002",
        "Siti"
    )

    transaksi1.tambah_produk(
        produk1,
        2
    )

    transaksi1.tambah_produk(
        diskon1,
        1
    )

    transaksi2.tambah_produk(
        produk2,
        2
    )

    transaksi2.tambah_produk(
        diskon2,
        1
    )

    transaksi1.tampilkan_transaksi()

    transaksi2.tampilkan_transaksi()

    print("\n--- PEMBAYARAN TRANSAKSI 1 ---")

    transaksi1.proses_pembayaran(
        100000
    )

    print("\n--- FACTORY METHOD ---")

    data_produk = {
        "kode": "P003",
        "nama": "Muffin",
        "harga": 18000,
        "stok": 12
    }

    produk3 = ProdukPastry.dari_dictionary(
        data_produk
    )

    produk3.tampilkan_info()

    while True:

        print("\n======================================")
        print("             MENU CRUD")
        print("======================================")
        print("1. Create - Tambah Produk")
        print("2. Read   - Tampilkan Produk")
        print("3. Update - Ubah Produk")
        print("4. Delete - Hapus Produk")
        print("5. Keluar")
        print("======================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            create_produk()

        elif pilihan == "2":
            read_produk()

        elif pilihan == "3":
            update_produk()

        elif pilihan == "4":
            delete_produk()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")
from abc import ABC, abstractmethod


class ProdukPastryDasar:
    def __init__(self, nama, harga):
        self._nama = nama
        self._harga = harga

    def tampilkan_info(self):
        return f"{self._nama} - Rp{self._harga:,.0f}"


class ProdukKue(ProdukPastryDasar):
    def __init__(self, nama, harga, rasa):
        super().__init__(nama, harga)
        self.rasa = rasa

    def tampilkan_info(self):
        return f"Kue: {self._nama} | Harga: Rp{self._harga:,.0f} | Rasa: {self.rasa}"


class ProdukRoti(ProdukPastryDasar):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

    def tampilkan_info(self):
        return f"Roti: {self._nama} | Harga: Rp{self._harga:,.0f} | Ukuran: {self.ukuran}"


class PromoPastry:
    def __init__(self, diskon):
        self.diskon = diskon

    def hitung_diskon(self, harga):
        return harga - (harga * self.diskon / 100)


class ProdukPromo(ProdukKue, PromoPastry):
    def __init__(self, nama, harga, rasa, diskon):
        ProdukKue.__init__(self, nama, harga, rasa)
        PromoPastry.__init__(self, diskon)

    def tampilkan_info(self):
        harga_akhir = self.hitung_diskon(self._harga)
        return (
            f"Produk Promo: {self._nama} | Harga: Rp{self._harga:,.0f} | "
            f"Rasa: {self.rasa} | Diskon: {self.diskon}% | "
            f"Harga Akhir: Rp{harga_akhir:,.0f}"
        )


class BahanPastry:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah


class ResepPastry:
    def __init__(self, nama_resep):
        self.nama_resep = nama_resep
        self.daftar_bahan = []

    def tambah_bahan(self, nama, jumlah):
        bahan = BahanPastry(nama, jumlah)
        self.daftar_bahan.append(bahan)

    def tampilkan_resep(self):
        print(f"Resep: {self.nama_resep}")
        for bahan in self.daftar_bahan:
            print(f"- {bahan.nama}: {bahan.jumlah}")


class TokoPastry:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self.daftar_produk = []

    def tambah_produk(self, produk):
        self.daftar_produk.append(produk)

    def tampilkan_produk(self):
        print(f"Toko: {self.nama_toko}")
        for produk in self.daftar_produk:
            hasil = produk.tampilkan_info()
            if hasil is not None:
                print(hasil)


class Pelanggan:
    def __init__(self, nama):
        self.nama = nama

    def melakukan_pemesanan(self, transaksi):
        print(f"{self.nama} melakukan pemesanan.")
        transaksi.tampilkan_transaksi()


class AktivitasPastry(ABC):
    def __init__(self, nama_aktivitas):
        self._nama_aktivitas = nama_aktivitas
        self.__kode_aktivitas = "ACT001"

    @abstractmethod
    def persiapkan(self):
        pass

    @abstractmethod
    def proses(self):
        pass

    def jalankan(self):
        print(f"\nAktivitas: {self._nama_aktivitas}")
        self.persiapkan()
        self.proses()


class MembuatKue(AktivitasPastry):
    def __init__(self, nama_aktivitas, jenis_kue):
        super().__init__(nama_aktivitas)
        self.jenis_kue = jenis_kue

    def persiapkan(self):
        print(f"Menyiapkan bahan untuk {self.jenis_kue}")

    def proses(self):
        print(f"Membuat kue jenis {self.jenis_kue}")


class MembuatRoti(AktivitasPastry):
    def __init__(self, nama_aktivitas, ukuran_roti):
        super().__init__(nama_aktivitas)
        self.ukuran_roti = ukuran_roti

    def persiapkan(self):
        print(f"Menyiapkan adonan roti ukuran {self.ukuran_roti}")

    def proses(self):
        print(f"Memanggang roti ukuran {self.ukuran_roti}")


class LaporanStok:
    def __init__(self, jumlah_produk):
        self.jumlah_produk = jumlah_produk

    def tampilkan_ringkasan(self):
        print(f"Jumlah produk tersedia: {self.jumlah_produk}")


class LaporanTransaksi:
    def __init__(self, total_transaksi):
        self.total_transaksi = total_transaksi

    def tampilkan_ringkasan(self):
        print(f"Total transaksi: Rp{self.total_transaksi:,.0f}")


def cetak_ringkasan(objek):
    objek.tampilkan_ringkasan()


class BahanPastryUkur:
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    def __add__(self, bahan_lain):
        if not isinstance(bahan_lain, BahanPastryUkur):
            return NotImplemented
        if self.nama != bahan_lain.nama:
            raise ValueError("Bahan harus memiliki nama yang sama.")
        return BahanPastryUkur(self.nama, self.jumlah + bahan_lain.jumlah)

    def __str__(self):
        return f"{self.nama}: {self.jumlah} gram"


def demo_tambahan():
    print("\n=== RELASI UML: ASOSIASI ===")
    pelanggan = Pelanggan("Andi")
    pelanggan.melakukan_pemesanan(transaksi1)

    print("\n=== RELASI UML: AGREGASI ===")
    toko = TokoPastry("Sweet Pastry Shop")
    toko.tambah_produk(produk1)
    toko.tambah_produk(diskon1)
    toko.tampilkan_produk()

    print("\n=== RELASI UML: KOMPOSISI ===")
    resep = ResepPastry("Chocolate Cake")
    resep.tambah_bahan("Tepung", "200 gram")
    resep.tambah_bahan("Cokelat", "100 gram")
    resep.tampilkan_resep()

    print("\n=== BUKTI ABSTRAKSI ===")
    try:
        AktivitasPastry("Aktivitas umum")
    except TypeError:
        print("Abstract class tidak dapat diinstansiasi.")
        print("TypeError")

    print("\n=== POLIMORFISME PEWARISAN ===")
    daftar_aktivitas = [
        MembuatKue("Produksi kue", "Cokelat"),
        MembuatRoti("Produksi roti", "Besar")
    ]
    for aktivitas in daftar_aktivitas:
        aktivitas.jalankan()

    print("\n=== DUCK TYPING ===")
    laporan_stok = LaporanStok(len(daftar_produk))
    laporan_transaksi = LaporanTransaksi(transaksi1.hitung_total())
    for laporan in [laporan_stok, laporan_transaksi]:
        cetak_ringkasan(laporan)

    print("\n=== OPERATOR OVERLOADING ===")
    bahan1 = BahanPastryUkur("Tepung", 200)
    bahan2 = BahanPastryUkur("Tepung", 150)
    print("Hasil penjumlahan:", bahan1 + bahan2)


if __name__ == "__main__":
    demo_tambahan()