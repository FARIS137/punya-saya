class persegipanjang:
    #member1 variabel
    panjang = ""
    lebar = ""
    #member2 konstruktor
    def __init__(self):
        print("\n Persegi panjang")
        self.p=int(input("panjang = "))
        self.l=int(input("lebar = "))
    def luaspersegipanjang(self):
        luas = self.p*self.l
        print('luas persegi panjang = ', luas)
    def kelilingpersegipanjang(self):
        keliling = 2*(self.l+self.p)
        print('keliling persegi panjang = ', keliling)

