class Mahasiswa:

    def __init__(self, nama, nim, jurusan):
        # method ini menerima tiga parameter yaitu nama, nim, dan jurusan
        self.Nama = nama
        #: Parameter ini digunakan untuk menyimpan nama mahasiswa yang akan diassign ke atribut Nama dalam objek.
        self.Nim = nim
        # Parameter ini digunakan untuk menyimpan NIM (Nomor Induk Mahasiswa) yang akan diassign ke atribut Nim dalam objek.
        self.Jurusan = jurusan
        # Parameter ini digunakan untuk menyimpan NIM (Nomor Induk Mahasiswa) yang akan diassign ke atribut Nim dalam objek.

    def tampilkan_info(self):
        print('-----------------------------------')
        print('Nama Mahasiswa :', self.Nama)
        print('NIM Mahasiwa   :', self.Nim)
        print('Jurusan        :', self.Jurusan.namaJurusan)
# Method tampilkan_info() digunakan untuk menampilkan informasi mahasiswa.
# Dengan menggunakan method ini, kita dapat dengan mudah mencetak informasi lengkap mengenai seorang mahasiswa,
# termasuk nama, NIM, dan nama jurusan yang sedang ditempuh oleh mahasiswa tersebut.


class Jurusan:
    def __init__(self, nama_jurusan):
        self.namaJurusan = nama_jurusan
        self.daftarMahasiswa = []
# Dengan menggunakan method ini, ketika objek dari kelas Jurusan dibuat, atribut-atribut
# dalam objek tersebut akan diinisialisasi sesuai dengan nilai-nilai yang diberikan saat pembuatan objek.

    def tambah_Mahasiswa(self, mahasiswa):
        # Method tambah_Mahasiswa(self, mahasiswa) digunakan untuk menambahkan objek mahasiswa ke dalam daftar
        # mahasiswa yang terkait dengan objek jurusan.
        self.daftarMahasiswa.append(mahasiswa)
        # Metode append() digunakan untuk menambahkan objek mahasiswa ke dalam daftarMahasiswa yang merupakan atribut objek jurusan.

    def tampilkan_Data(self):
        print('Daftar Mahasiswa di jurusan', self.namaJurusan)
        # Dalam method ini, akan dicetak judul "Daftar Mahasiswa di jurusan" diikuti dengan nama jurusan (self.namaJurusan).
        for i, mahasiswa in enumerate(self.daftarMahasiswa, start=1):
            # setiap objek mahasiswa dalam self.daftarMahasiswa akan ditampilkan dengan nomor urut, nama mahasiswa (mahasiswa.Nama),
            # dan NIM mahasiswa (mahasiswa.Nim).
            print(f"{i}. Nama: {mahasiswa.Nama}")
            # mengeluarkan output nama mahasiswa
            print(f"   Nim : {mahasiswa.Nim}")
            # mengeluarkan output nim mahasiswa
            print()


class Universitas:

    def __init__(self, nama_universitas):
        self.namaUniversitas = nama_universitas
    # Parameter ini digunakan untuk menyimpan nama universitas yang akan diassign ke atribut namaUniversitas dalam objek.
        self.daftarJurusan = []
        # menginisialisasi atribut daftarJurusan sebagai sebuah list kosong.

    def tambah_jurusan(self, jurusan):
        self.daftarJurusan.append(jurusan)
# digunakan untuk menambahkan objek jurusan ke dalam daftar jurusan yang terkait dengan objek universitas.

    def tampilkan_daftar_jurusan(self):
        print('\n')
        # digunakan untuk menampilkan daftar jurusan yang terdapat dalam objek universitas.
        print("Daftar Jurusan di Universitas", self.namaUniversitas)
        # mencetak judul "Daftar Jurusan di Universitas" diikuti dengan nama universitas (self.namaUniversitas).
        for i, jurusan in enumerate(self.daftarJurusan, start=1):
            print(f"{i}. {jurusan.namaJurusan}")
            # setiap objek jurusan dalam self.daftarJurusan akan ditampilkan dengan nomor
            # urut dan nama jurusan (jurusan.namaJurusan).
        print()


# Buat objek Universitas dengan nama "XYZ"
xyz_university = Universitas("XYZ")

# Input jumlah jurusan
jumlah_jurusan = int(input("Masukkan jumlah jurusan di universitas: "))

# Input data jurusan
for i in range(jumlah_jurusan):
    nama_jurusan = input(f"Masukkan nama jurusan ke-{i+1}: ")
    jurusan = Jurusan(nama_jurusan)
    xyz_university.tambah_jurusan(jurusan)

    # Input jumlah mahasiswa per jurusan
    jumlah_mahasiswa = int(
        input(f"Masukkan jumlah mahasiswa di jurusan {nama_jurusan}: "))

    # Input data mahasiswa
    for j in range(jumlah_mahasiswa):
        nama_mahasiswa = input("Masukkan nama mahasiswa: ")
        nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
        mahasiswa = Mahasiswa(nama_mahasiswa, nim_mahasiswa, jurusan)
        jurusan.tambah_Mahasiswa(mahasiswa)


# Tampilkan daftar jurusan yang ada di Universitas XYZ
xyz_university.tampilkan_daftar_jurusan()

# Tampilkan daftar mahasiswa per jurusan di Universitas XYZ
for jurusan in xyz_university.daftarJurusan:
    jurusan.tampilkan_Data()
