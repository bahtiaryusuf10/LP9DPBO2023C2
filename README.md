### Saya Muhammad Yusuf Bahtiar NIM 2107980 mengerjakan Latihan Praktikum 9 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

<br>

## Deskripsi Tugas

Buatlah program menggunakan bahasa pemrograman PHP dengan spesifikasi sebagai berikut:

1. Lengkapi fitur summary
2. Buat landing Page (button yg ngarah ke halaman daftar residen)
3. Tampilin gambar
4. Tambahin 1 metode yang masih relevan untuk setiap kelas

<br>

## Desain Program

Program didesain menggunakan 5 class, yaitu:

1. Class Hunian, class ini merupakan superclass (parentclass) dari class lainnya. Dibuat dengan tujuan untuk merepresentasikan suatu tempat hunian yang memiliki beberapa atribut, diantaranya :

   - jenis untuk jenis hunian
   - jml_penghuni untuk jumlah penghuni yang menempati hunian
   - jml_kamar untuk jumlah kamar yang terdapat pada hunian
   - lokasi untuk lokasi tempat hunian tersebut dibangun

   pada class ini tersedia juga beberapa method, diantaranya :

   - get_jenis untuk mengambil data jenis hunian
   - get_jml_penghuni untuk mengambil data jumlah penghuni
   - get_jml_kamar untuk mengambil data jumlah kamar
   - get_lokasi untuk mengambil data lokasi
   - get_dokumen untuk mengambil data dokumen kepemilikan hunian (diimplementasikan di subclass)
   - get_summary untuk mengambil data informasi hunian

2. Class Apartemen, class ini merupakan subclass (childclass) dari class hunian. Dibuat dengan tujuan untuk merepresentasikan suatu apartemen yang memiliki beberapa atribut tambahan, diantaranya :

   - nama_pemilik untuk nama pemilik apartemen
   - harga_jual untuk harga jual apartemen
   - foto untuk dokumen gambar apartemen

   pada class ini tersedia juga beberapa method, diantaranya :

   - get_dokumen untuk mengimplementasikan method yang ada pada superclass, di sini digunakan untuk menampilkan SHMSRS
   - get_nama_pemilik untuk mengambil data nama pemilik apartemen
   - get_foto untuk mengambil data gambar apartemen
   - get_detail untuk mengambil data informasi secara mendetail dari apartemen

3. Class Indekos, class ini merupakan subclass (childclass) dari class hunian. Dibuat dengan tujuan untuk merepresentasikan suatu indekos yang memiliki beberapa atribut tambahan, diantaranya :

   - nama_pemilik untuk nama pemilik indekos
   - nama_penghuni untuk nama penghuni indekos
   - harga_sewa untuk harga sewa indekos per bulan
   - foto untuk dokumen gambar indekos

   pada class ini tersedia juga beberapa method, diantaranya :

   - get_dokumen untuk mengimplementasikan method yang ada pada superclass, di sini digunakan untuk menampilkan Bukti kontrak Indekos
   - get_nama_pemilik untuk mengambil data nama pemilik indekos
   - get_nama_penghuni untuk mengambil data nama penghuni indekos
   - get_foto untuk mengambil data gambar indekos
   - get_summary untuk mengambil data informasi indekos
   - get_detail untuk mengambil data informasi secara mendetail dari indekos

4. Class Rumah, class ini merupakan subclass (childclass) dari class hunian. Dibuat dengan tujuan untuk merepresentasikan suatu rumah yang memiliki beberapa atribut tambahan, diantaranya :

   - nama_pemilik untuk nama pemilik rumah
   - harga_jual untuk harga jual rumah
   - foto untuk dokumen gambar rumah

   pada class ini tersedia juga beberapa method, diantaranya :

   - get_dokumen untuk mengimplementasikan method yang ada pada superclass, di sini digunakan untuk menampilkan IMB
   - get_nama_pemilik untuk mengambil data nama pemilik rumah
   - get_foto untuk mengambil data gambar rumah
   - get_detail untuk mengambil data informasi secara mendetail dari rumah

5. Class Villa (class tambahan), class ini merupakan subclass (childclass) dari class hunian. Dibuat dengan tujuan untuk merepresentasikan suatu villa yang memiliki beberapa atribut tambahan, diantaranya :

   - nama_pemilik untuk nama pemilik villa
   - harga_jual untuk harga jual villa
   - foto untuk dokumen gambar villa

   pada class ini tersedia juga beberapa method, diantaranya :

   - get_dokumen untuk mengimplementasikan method yang ada pada superclass, di sini digunakan untuk menampilkan SHM
   - get_nama_pemilik untuk mengambil data nama pemilik villa
   - get_foto untuk mengambil data gambar villa
   - get_detail untuk mengambil data informasi secara mendetail dari villa

<br>

## Alur Program

Program akan menampilkan halaman `Landing Page` yang berisi konten ucapan selamat datang, gambar aplikasi, dan penjelasan aplikasi. Selain itu, tersedia juga tombol `Mulai` yang ketika di-klik, maka pengguna akan diarahkan menuju halaman `Home`.

1. Jika pengguna meng-klik tombol `Details` hunian yang ada pada kolom `Aksi`, maka akan menampilkan halaman `Detail` yang berisi detail dari hunian yang dipilih tersebut. Pada halaman `Detail` terdapat tombol `Close`, yang ketika di-klik akan mengembalikan pengguna ke halaman `Home`.
2. Jika pengguna meng-klik tombol `Add Data`, maka akan menampilkan halaman `Form Jenis Hunian` yang berisi field dropdown pilihan jenis hunian (berdasarkan subclass yang dibuat). Pada halaman `Form Jenis Hunian` juga tersedia tombol `Close` yang ketika di-klik akan mengembalikan pengguna ke halaman `Home` dan tombol `Next` yang ketika di-klik akan menampilkan halaman `Form Add Data Hunian` yang berisi field data hunian yang dibutuhkan, di mana field tersebut akan sesuai dengan jenis hunian yang telah dipilih sebelumnya.
3. Ketika pengguna hendak menambahkan data, pada halaman `Form Add Data Hunian` terdapat tombol `Save` yang berguna untuk menyimpan data baru ke dalam list hunian ketika di-klik.
4. Jika pengguna meng-klik tombol `Exit`, maka akan langsung menghentikan aplikasi.

\*Note : Untuk saat ini, setiap penambahan data hunian baru melalui aplikasi tidak tersedia upload foto. Jadi, jika pengguna ingin menggunakan foto berbeda, penambahan datanya harus manual melalui file `main.py`.

<br>

## Dokumentasi

- Bukti Coba Database
  ![Bukti-Coba-Database](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/41cc384a-abe4-4954-9f1f-26eb6a7037b2)

- Landing Page
  ![Landing-Page](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/efb97d6d-c458-426a-8056-661dff706816)

- Home
  ![Home](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/9f3e4d4a-9773-407c-aef0-1eb949ea4f19)

- Detail Apartemen
  ![Detail-Apartemen](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/fbdc22b9-bb7a-489f-bcaa-7b2235ea5a0d)

- Detail Rumah
  ![Detail-Rumah](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/bf361836-c01a-4edb-9d89-8d34fed0d696)

- Detail Indekos
  ![Detail-Indekos](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/5d70f1ed-6c2d-4ecc-8962-5fbe91d545e1)

- Detail Villa
  ![Detail-Villa](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/67651fb6-bdc8-4fe3-9a42-9ef5824d65ce)

- Opsi Jenis Hunian
  ![Opsi-Jenis-Hunian](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/1ffe77d5-49eb-49f7-9ff8-27c008c26768)

- Form Add Indekos
  ![Form-Add-Indekos](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/86e70248-a110-4d8c-a7dc-cf45a401695c)

- Form Add Hunian Lain (example : Villa)
  ![Form-Add-Villa](https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/bcd1d37b-7305-421a-ab61-3cf0b3a6c8dc)

- Video

  https://github.com/bahtiaryusuf10/LP9DPBO2023C2/assets/100776170/1b6c1941-5bac-4201-811e-520141b2a0c7
