class Employees:
    print("Yeni bir sınıf oluşturuldu...")
    unvan = "Personel"

    def __init__(self):
        print("Yeni bir personel oluşturuldu...")
        self.isim = "Ayşegül"
        self.yetenekler = ["Android", "Kotlin", "Java"]
        self.unvan = "Android Dev."
        self.gunSayisi = 0

    def calis(self):
        self.gunSayisi += 1
        print("Şu anda çalışıyor, çalıştığı gün ise : ", self.gunSayisi)


ahmet = Employees()

ahmet.isim = "Testt"

ahmet.calis()
ahmet.calis()
ahmet.calis()

print(ahmet.gunSayisi)
