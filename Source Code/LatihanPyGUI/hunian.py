class Hunian:
    # konstruktor
    def __init__(self, jenis, jml_penghuni=1, jml_kamar=1, lokasi=""):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.lokasi = lokasi

    # untuk mengambil jenis hunian
    def get_jenis(self):
        return self.jenis

    # untuk mengambil jumlah penghuni
    def get_jml_penghuni(self):
        return self.jml_penghuni

    # untuk mengambil jumlah kamar
    def get_jml_kamar(self):
        return self.jml_kamar
    
    # untuk mengambil lokasi (method yang ditambahkan)
    def get_lokasi(self):
        return self.lokasi

    # untuk mengambil dokumen hunian (yang akan diimplementasikan pada subclass)
    def get_dokumen(self):
        pass

    # untuk mengambil informasi jenis hunian dan ditempati oleh berapa orang
    def get_summary(self):
        return (
            "Hunian "
            + self.jenis
            + ", ditempati oleh "
            + str(self.jml_penghuni)
            + " orang."
        )