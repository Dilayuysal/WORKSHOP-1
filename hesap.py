#Banka
class Hesap:
    def __init__(self, hesap_sahibi, hesap_numarasi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_numarasi = hesap_numarasi
        self.__bakiye = bakiye   
    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} kadar para yatırılıyor.")
        else:
            print("Miktar 0'dan buyuk olmalıdır.")
    def para_cek(self, miktar):
        if miktar<=self.__bakiye and miktar>0:
            self.__bakiye -= miktar
            print(f"{miktar} kadar para çekiliyor.")
        else:
            print("Bakiye yetersiz veya miktar 0'dan buyuk olmalıdır.")
    def bakiye_goster(self):
        print(f"Bakiye: {self.__bakiye}")
        return self.__bakiye
    
class VadesizHesap(Hesap):
    pass

class VadeliHesap(Hesap):
    def __init__(self,hesap_sahibi,hesap_numarasi,faiz_orani=0.5):
        super().__init__(hesap_sahibi, hesap_numarasi,faiz_orani)
        self.faiz_orani = faiz_orani
    def para_cek(self, miktar):
        if miktar <= self.bakiye_goster() * self.faiz_orani:
            super().para_cek(miktar)
        else:
            print("Bakiye yetersiz veya miktar 0'dan buyuk olmalıdır.")  
    def faiz_hesapla(self):
        faiz = self.bakiye_goster() * self.faiz_orani
        self.para_yatir(faiz)
        print(f"Faiz eklendi: Yeni Bakiye: {self.bakiye_goster()} ")



hesap1 = VadesizHesap("Ersin Alçin", "12345", 5000)
hesap1.bakiye_goster()
hesap1.para_yatir(1000)
hesap1.para_cek(3000)
hesap1.bakiye_goster()

print("\nVadeli Hesap İşlemleri")
hesap2 = VadeliHesap("Dilay Uysal", "67890",0)
hesap2.bakiye_goster()
hesap2.para_yatir(1000)
hesap2.faiz_orani = 0.05
hesap2.faiz_hesapla()








