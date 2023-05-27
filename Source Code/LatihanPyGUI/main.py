from villa import Villa
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import Image, ImageTk
import ttkbootstrap as ttk

# membuat list hunian
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "Malang", 250000000, "Apartement.jpg"))
hunians.append(Rumah("Sekar MK", 5, 2, "Surabaya", 450000000, "Rumah.jpg"))
hunians.append(Indekos("Bp. Romi", "Cahya", "Yogyakarta", 750000, "Indekos.jpeg"))
hunians.append(Rumah("Satria", 1, 4, "Jakarta", 400000000, "Rumah.jpg"))
hunians.append(Villa("Maikel", 9, 17, "Bogor", 7500000000))

# membuat window dengan tema darkly
root = ttk.Window(themename="darkly")

# mengatur agar ukuran window 760px x 420px dan selalu berada di tengah layar
width = 760
height = 420
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2) - 100
root.geometry(f"{width}x{height}+{x}+{y}")

# agar window hanya dapat diubah ukurannya secara verttikal
root.resizable(False, True)
root.title("Praktikum DPBO Python")


# untuk mengambil data photo dan mengatur ukurannya saat ditampilkan
def set_image(name, width, height):
    image = Image.open("./LatihanPyGUI/images/" + name)
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)

    return photo


# untuk menampilkan window detail dari hunian yang dipilih
def details(index):
    # membuat window baru
    top = Toplevel()

    # mengatur judul window sesuai dengan jenis hunian
    top.title("Detail " + hunians[index].get_jenis())

    # mengatur agar ukuran window 690px x 580px dan selalu berada di tengah layar
    width = 690
    height = 580
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2) - 100
    top.geometry(f"{width}x{height}+{x}+{y}")

    # agar window hanya dapat diubah ukurannya secara horizontal
    top.resizable(True, False)

    # menampilkan gambar hunian yang dipilih
    photo = set_image(hunians[index].get_foto(), 300, 200)
    image_label = Label(top, image=photo)
    image_label.image = photo
    image_label.pack(side=TOP, padx=30, pady=20)

    # menampilkan section summary data hunian
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(
        d_frame,
        text="Summary\n"
        + hunians[index].get_detail()
        + hunians[index].get_summary()
        + "\n"
        + hunians[index].get_dokumen(),
        anchor="w",
        justify=LEFT,
    ).grid(row=0, column=0, sticky="w")

    # menambahkan button untuk menutup window
    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=10, pady=10)
    b_close = Button(btn, text="Close", command=top.destroy)
    b_close.grid(row=0, column=0)


# untuk menambahkan data hunian baru
def add_data(index):
    # membuat window baru
    top = Toplevel()
    top.title("Add Data")

    # mengatur agar ukuran window 427px x 390px dan selalu berada di tengah layar
    width = 427
    height = 390
    x = (top.winfo_screenwidth() // 2) - (width // 2)
    y = (top.winfo_screenheight() // 2) - (height // 2) - 100
    top.geometry(f"{width}x{height}+{x}+{y}")

    # agar window tidak dapat diubah ukurannya
    top.resizable(False, False)

    # menampilkan section form pilih jenis hunian
    d_frame = LabelFrame(top, text="Form Jenis Hunian", padx=10, pady=10)
    d_frame.pack(padx=50, pady=60)

    # field jenis hunian (dropdown)
    label_jenis_hunian = Label(d_frame, text="Jenis Hunian")
    label_jenis_hunian.pack(side=LEFT)
    jenis_hunian = StringVar(top)
    jenis_hunian.set(hunians[index].get_jenis())
    jenis_hunian_dropdown = OptionMenu(d_frame, jenis_hunian, *["Rumah", "Apartemen", "Indekos", "Villa"])
    jenis_hunian_dropdown.pack(side=RIGHT)

    # untuk menampilkan field form yang harus diisi sesuai dengan jenis hunian yang dipilih
    def form_add():
        # menghapus konten sebelumnya yang ada pada window
        d_frame.destroy()
        label_jenis_hunian.destroy()
        jenis_hunian_dropdown.destroy()
        b_next.destroy()
        b_close.destroy()

        # menampilkan section form data hunian
        frame = LabelFrame(top, text="Form Add Data " + jenis_hunian.get(), padx=10, pady=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        if (jenis_hunian.get() == "Indekos"):  # jika yang akan ditambahkan adalah jenis indekos, maka hanya ada 4 field yang harus diisi
            # field nama pemilik
            label_pemilik = Label(frame, text="Nama Pemilik")
            label_pemilik.grid(row=0, column=0)
            value1 = Entry(frame)
            value1.grid(row=0, column=1, pady=10)

            # field nama penghuni
            label_penghuni = Label(frame, text="Nama Penghuni")
            label_penghuni.grid(row=1, column=0)
            value2 = Entry(frame)
            value2.grid(row=1, column=1, pady=10)

            # field lokasi
            label_lokasi = Label(frame, text="Lokasi")
            label_lokasi.grid(row=2, column=0)
            value3 = Entry(frame)
            value3.grid(row=2, column=1, pady=10)

            # field harga Sewa per Bulan
            label_harga_sewa = Label(frame, text="Harga Sewa per Bulan")
            label_harga_sewa.grid(row=3, column=0)
            value4 = Entry(frame)
            value4.grid(row=3, column=1, pady=10)
        else:  # jika yang akan ditambahkan adalah jenis rumah, apartemen, atau villa, maka ada 6 field yang harus diisi
            # field nama pemilik
            label_pemilik = Label(frame, text="Nama Pemilik")
            label_pemilik.grid(row=1, column=0, padx=5)
            value1 = Entry(frame)
            value1.grid(row=1, column=1, padx=15, pady=10)

            # field jumlah kamar
            label_jumlah_kamar = Label(frame, text="Jumlah Kamar")
            label_jumlah_kamar.grid(row=2, column=0, padx=5)
            value2 = Entry(frame)
            value2.grid(row=2, column=1, padx=15, pady=10)

            # field jumlah penghuni
            label_jumlah_penghuni = Label(frame, text="Jumlah Penghuni")
            label_jumlah_penghuni.grid(row=3, column=0, padx=5)
            value3 = Entry(frame)
            value3.grid(row=3, column=1, padx=15, pady=10)

            # field lokasi
            label_lokasi = Label(frame, text="Lokasi")
            label_lokasi.grid(row=4, column=0, padx=5)
            value4 = Entry(frame)
            value4.grid(row=4, column=1, padx=15, pady=10)

            # field harga jual
            label_Harga_Jual = Label(frame, text="Harga Jual")
            label_Harga_Jual.grid(row=5, column=0, padx=5)
            value5 = Entry(frame)
            value5.grid(row=5, column=1, padx=15, pady=10)

        # untuk menyimpan data ke dalam list hunians
        def save_data():
            # mengambil jenis hunian yang dipilih
            jenis = jenis_hunian.get()
            if (jenis == "Apartemen"):  # jika yang akan ditambahkan adalah jenis apartemen
                # maka akan menambahkan data ke dalam list hunians dengan class apartemen
                hunians.append(Apartemen(value1.get(), int(value3.get()), int(value2.get()), value4.get(), int(value5.get())))
            elif jenis == "Rumah":  # jika yang akan ditambahkan adalah jenis rumah
                # maka akan menambahkan data ke dalam list hunians dengan class rumah
                hunians.append(Rumah(value1.get(), int(value3.get()), int(value2.get()), value4.get(), int(value5.get())))
            elif jenis == "Indekos":  # jika yang akan ditambahkan adalah jenis indekos
                # maka akan menambahkan data ke dalam list hunians dengan class indekos
                hunians.append(Indekos(value1.get(), value2.get(), value3.get(), int(value4.get())))
            elif jenis == "Villa":  # jika yang akan ditambahkan adalah jenis villa
                # maka akan menambahkan data ke dalam list hunians dengan class villa
                hunians.append(Villa(value1.get(), int(value3.get()), int(value2.get()), value4.get(), int(value5.get())))

            # menghapus window field form
            top.destroy()

            # menampilkan notifikasi bahwa data berhasil ditambahkan
            print("Data added")

            # mereset tabel yang ada pada window utama
            reset_table()

        # menambahkan tombol save untuk men-trigger fungsi save_data
        btn2 = LabelFrame(top, padx=0, pady=0)
        btn2.grid(row=1, column=0, padx=10, pady=10)
        b_save = Button(btn2, text="Save", command=save_data)
        b_save.grid(row=0, column=1)

    # menambahkan tombol close untuk menutup window form add data
    b_close = Button(top, text="Close", command=top.destroy)
    b_close.pack(side=LEFT, padx=105)

    # menambahkan tombol next untuk menampilkan field form
    b_next = Button(top, text="Next", command=form_add)
    b_next.pack(side=LEFT, padx=10)


# section tabel data hunian pada window utama
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)


# untuk mereset tabel yang akan ditampilkan pada window utama
def reset_table():
    # menghapus konten yang ada pada landing page
    title_label.destroy()
    image_label.destroy()
    text_label.destroy()
    show_table_button.destroy()

    # menghapus konten yang ada pada tabel
    for widget in frame.winfo_children():
        widget.destroy()

    # membuat kembali tabel dengan menambahkan header terlebih dahulu
    # header kolom ke-1 dengan nama 'No'
    headerColumn1 = Label(frame, text="No", width=5, borderwidth=1, relief="solid")
    headerColumn1.config(highlightbackground="white", highlightthickness=1)
    headerColumn1.grid(row=0, column=0, pady=5)

    # header kolom ke-2 dengan nama 'Jenis Hunian'
    headerColumn2 = Label(frame, text="Jenis Hunian", width=15, borderwidth=1, relief="solid")
    headerColumn2.config(highlightbackground="white", highlightthickness=1)
    headerColumn2.grid(row=0, column=1, pady=5)

    # header kolom ke-3 dengan nama 'Pemilik / Penghuni'
    headerColumn3 = Label(frame, text="Pemilik / Penghuni", width=40, borderwidth=1, relief="solid")
    headerColumn3.config(highlightbackground="white", highlightthickness=1)
    headerColumn3.grid(row=0, column=2, pady=5)

    # header kolom ke-4 dengan nama 'Aksi'
    headerColumn4 = Label(frame, text="Aksi", width=10, borderwidth=1, relief="solid")
    headerColumn4.config(highlightbackground="white", highlightthickness=1)
    headerColumn4.grid(row=0, column=3, pady=5)

    # menampilkan semua data hunian yang ada pada list hunians
    for index, h in enumerate(hunians):
        # menampilkan nomor
        idx = Label(frame, text=str(index + 1), width=5, borderwidth=1, relief="solid")
        idx.config(highlightbackground="white", highlightthickness=1)
        idx.grid(row=index + 1, column=0)

        # menampilkan jenis hunian
        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.config(highlightbackground="white", highlightthickness=1)
        type.grid(row=index + 1, column=1)

        # menampilkan nama pemilik / penghuni
        if h.get_jenis() != "Indekos":
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.config(highlightbackground="white", highlightthickness=1)
            name.grid(row=index + 1, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.config(highlightbackground="white", highlightthickness=1)
            name.grid(row=index + 1, column=2)

        # menambahkan tombol detail untuk aksi menampilkan detail hunian
        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index + 1, column=3)

    # menambahkan tombol exit untuk keluar aplikasi
    b_exit = Button(text="Exit", command=root.quit)
    b_exit.pack(side=LEFT, padx=175)

    # menambahkan tombol add data untuk untuk menambahkan data hunian (menampilkan window form add data)
    b_add = Button(text="Add Data", command=lambda: add_data(index))
    b_add.pack(side=LEFT, padx=100)


# Landing Page
title_label = ttk.Label(master=root, text="Selamat datang di Aplikasi Hunian!", font=("Verdana", 18))
title_label.pack(pady=10)

# menampilkan gambar pada landing page
photo = set_image("Kota-Baru-Parahyangan.jpeg", 360, 240)
image_label = Label(root, image=photo)
image_label.image = photo
image_label.pack(side=LEFT, padx=30)

# menampilkan teks yang telah di-wraping pada landing page
text = "Aplikasi hunian adalah aplikasi yang memberikan informasi mengenai berbagai jenis hunian, di mana pengguna dapat melihat data dari hunian dan juga dapat menggunakan fitur add data untuk menambahkan suatu data hunian."
text_label = Text(root, wrap="word", height=7)
text_label.insert("1.0", text)
text_label.configure(state="disabled", font=("Geneva", 9))
text_label.pack(padx=20, expand=True)

# menambahkan tombol mulai untuk memulai aplikasi (menampilkan window utama / tabel data hunian)
show_table_button = ttk.Button(root, text="Mulai", command=reset_table)
show_table_button.pack(padx=10, expand=True)

root.mainloop()
