class Lingkaran:
    #memberi variabel
    jari2 = "phi"
    #konstruktor 
    def __init__(self):
        self.r=int(input("jari-jari = "))
    def luaslingkaran(self):
        phi=3.14
        luas = phi*self.r**2
        print("luas lingkaran = ",luas)
    def kelilinglingkaran(self):
        phi=3.14
        keliling = 2*phi*self.r
        print("keliling lingkaran = ",keliling)
   
