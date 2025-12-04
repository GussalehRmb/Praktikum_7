class NilaiMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self):
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Masukkan nama mahasiswa: ")
        nilai = input("Masukkan nilai: ")

        if nama in self.data:
            print("Data dengan nama tersebut sudah ada!")
        else:
            self.data[nama] = nilai
            print("Data berhasil ditambahkan.")

    def tampilkan(self):
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.data:
            print("Belum ada data.")
        else:
            for nama, nilai in self.data.items():
                print(f"- {nama} : {nilai}")

    def hapus(self):
        print("\n=== Hapus Data Mahasiswa ===")
        nama = input("Masukkan nama yang ingin dihapus: ")

        if nama in self.data:
            del self.data[nama]
            print("Data berhasil dihapus.")
        else:
            print("Data tidak ditemukan.")

    def ubah(self):
        print("\n=== Ubah Data Mahasiswa ===")
        nama = input("Masukkan nama yang ingin diubah: ")

        if nama in self.data:
            nilai_baru = input("Masukkan nilai baru: ")
            self.data[nama] = nilai_baru
            print("Data berhasil diubah.")
        else:
            print("Data tidak ditemukan.")
            
def main():
    app = NilaiMahasiswa()

    while True:
        print("\n===== MENU =====")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            app.tambah()
        elif pilihan == "2":
            app.tampilkan()
        elif pilihan == "3":
            app.hapus()
        elif pilihan == "4":
            app.ubah()
        elif pilihan == "5":
            print("Keluar program...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
