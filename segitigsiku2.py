class Segitigasiku2:
    #member1 variabel
    alas = ""
    tinggi = ""
    #member2 konstruktor
    def __init__(self):
        print("\n Segitiga siku-siku")
        self.a=int(input("alas = "))
        self.t=int(input("tinggi = "))
    def luassegitigasiku2(self):
        luas = 0.5*self.a*self.t
        print("luas segitiga siku2 =", luas)
    def kelilingsegitigasiku2(self):
        keliling = self.a+self.t*2
        print("keliling segitiga siku2 =", keliling)

