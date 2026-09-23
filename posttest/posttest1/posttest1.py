from abc import ABC, abstractmethod
class ProdukPastry(ABC):
    # Atribut kelas
    nama_toko = "Sweet Pastry"
    total_produk = 0
    kategori_toko = "Pastry & Bakery"

    def __init__(self, kode_produk, nama_produk, harga, stok):
        # Atribut instance public
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

        # Atribut instance private
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

        # Atribut instance
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

    # Atribut kelas
    nama_toko = "Sweet Pastry"
    biaya_layanan = 2000
    total_transaksi = 0

    def __init__(self, nomor_transaksi, nama_pelanggan):
        # Atribut instance
        self.nomor_transaksi = nomor_transaksi
        self.nama_pelanggan = nama_pelanggan
        self.daftar_produk = []

        # Atribut private
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