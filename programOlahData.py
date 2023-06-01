class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.Nama = nama
        self.Nim = nim
        self.Jurusan = jurusan

    def tampilkan_info(self):
        print('-----------------------------------')
        print('Nama Mahasiswa :', self.Nama)
        print('NIM Mahasiwa   :', self.Nim)
        print('Jurusan        :', self.Jurusan.namaJurusan)


class Jurusan:
    def __init__(self, nama_jurusan):
        self.namaJurusan = nama_jurusan
        self.daftarMahasiswa = []

    def tambah_Mahasiswa(self, mahasiswa):
        self.daftarMahasiswa.append(mahasiswa)

    def tampilkan_Data(self):
        print('Daftar Mahasiswa di jurusan', self.namaJurusan)
        for i, mahasiswa in enumerate(self.daftarMahasiswa, start=1):
            print(f"{i}. Nama: {mahasiswa.Nama}")
            print(f"   Nim : {mahasiswa.Nim}")
            print()


class Universitas:
    def __init__(self, nama_universitas):
        self.namaUniversitas = nama_universitas
        self.daftarJurusan = []

    def tambah_jurusan(self, jurusan):
        self.daftarJurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.namaUniversitas)
        for i, jurusan in enumerate(self.daftarJurusan, start=1):
            print(f"{i}. {jurusan.namaJurusan}")
        print()

# 1. Implementasikan kelas Mahasiswa, Jurusan, dan Universitas
# (tidak perlu menulis di sini karena sudah dijelaskan di atas)


# 2. Buat objek Universitas dengan nama "XYZ University"
xyz_university = Universitas("XYZ University")

# 3. Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ
teknik_informatika = Jurusan("Teknik Informatika")
xyz_university.tambah_jurusan(teknik_informatika)

# 4. Buat objek Mahasiswa dengan nama "Kalian masing", NIM "Kalian masing", dan masukkan ke dalam Jurusan Teknik Informatika di Universitas XYZ
mahasiswa_1 = Mahasiswa(
    "M. FEBRI ARDIANSYAH", "G1A022049", teknik_informatika)
teknik_informatika.tambah_Mahasiswa(mahasiswa_1)


# 5. Buat objek Jurusan dengan nama "Teknik Komputer" dan tambahkan ke dalam Universitas XYZ
teknik_komputer = Jurusan("Teknik Komputer")
xyz_university.tambah_jurusan(teknik_komputer)

# 6. Buat objek Mahasiswa dan tambahkan ke dalam Jurusan Teknik Komputer di Universitas XYZ
mahasiswa_2 = Mahasiswa("John Doe", "G1A022050", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_2)

mahasiswa_3 = Mahasiswa("Jane Smith", "G1A022051", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_3)

mahasiswa_4 = Mahasiswa("Alex Johnson", "G1A022052", teknik_komputer)
teknik_komputer.tambah_Mahasiswa(mahasiswa_4)

# 8. Tampilkan daftar jurusan yang ada di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# 7. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Komputer di Universitas XYZ
teknik_komputer.tampilkan_Data()


# 9. Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ
teknik_informatika.tampilkan_Data()
# 10. Objek-objek yang telah dibuat sebelumnya

print('\n')
print('Data Mahasiswa')
mahasiswa_1.tampilkan_info()
mahasiswa_2.tampilkan_info()
mahasiswa_3.tampilkan_info()
mahasiswa_4.tampilkan_info()
mahasiswa_1.tampilkan_info()
