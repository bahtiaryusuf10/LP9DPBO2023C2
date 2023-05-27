from hunian import Hunian

class Indekos(Hunian):
    # konstruktor
    def __init__(self, nama_pemilik, nama_penghuni, lokasi, harga_sewa, foto = "Indekos.jpeg"):
        super().__init__("Indekos", lokasi = lokasi)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_sewa = harga_sewa
        self.foto = foto

    # mengimplementasikan method abstract dari superclass 
    def get_dokumen(self):
        return ("Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + ".")

    # untuk mengambil nama pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik

    # untuk mengambil nama penghuni
    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    # untuk mengambil foto indekos (method yang ditambahkan)
    def get_foto(self):
        return self.foto
    
    # untuk mengambil informasi jenis hunian
    def get_summary(self):
        return "Hunian Indekos."

    # untuk mengambil detail indekos
    def get_detail(self):
        return (
            "Pemilik : "
            + self.nama_pemilik
            + "\nJumlah Kamar : "
            + str(self.jml_kamar)
            + "\nLokasi : "
            + str(super().get_lokasi())
            + "\nHarga Sewa : Rp"
            + format(self.harga_sewa, ',').replace(",", ".") + "/bulan"
            + "\n"
        )
