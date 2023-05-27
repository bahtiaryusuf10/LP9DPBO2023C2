from hunian import Hunian

class Villa(Hunian):
    # konstruktor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, lokasi, harga_jual, foto = "Villa.jpg"):
        super().__init__("Villa", jml_penghuni, jml_kamar, lokasi = lokasi)
        self.nama_pemilik = nama_pemilik
        self.harga_jual = harga_jual
        self.foto = foto
        
    # mengimplementasikan method abstract dari superclass
    def get_dokumen(self):
        return ("Sertifikat Hak Milik (SHM) a/n " + self.nama_pemilik + ".")
        
    # untuk mengambil nama pemilik
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # untuk mengambil foto villa (method yang ditambahkan)
    def get_foto(self):
        return self.foto
    
    # untuk mengambil detail villa
    def get_detail(self):
        return (
            "Pemilik : "
            + self.nama_pemilik
            + "\nJumlah Kamar : "
            + str(self.jml_kamar)
            + "\nLokasi : "
            + str(super().get_lokasi())
            + "\nHarga Jual : Rp"
            + format(self.harga_jual, ',').replace(",", ".")
            + "\n"
        )