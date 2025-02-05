
"""
Kütüphane Yönetim Sistemi (Encapsulation, Composition, Exception Handling)
Bu projede bir kütüphane sistemini modelleyeceğiz.
Şartlar:
Kitap sınıfı:
Kitap adı, yazar, sayfa sayısı, ISBN bilgilerini içermeli.
Kutuphane sınıfı:
Kitap ekleme (kitap_ekle(kitap)), kitap kaldırma (kitap_sil(isbn)), tüm kitapları gösterme (kitaplari_goster()) metodları olmalı.
Exception Handl,
ing (Hata Yakalama): Bir kitap zaten ekliyse hata fırlatmalı.
"""

class  Kitap:
    def __init__(self,kitap_adi,yazar,sayfa_sayisi,ISBN):
        self.kitap_adi=kitap_adi,
        self.yazar=yazar,
        self.sayfa_sayisi=sayfa_sayisi,
        self.isbn=ISBN
    
class Kutuphane:
    def __init__(self,kitaplar):
        self.kitaplar=kitaplar
    def kitap_ekle(self,kitap):
        if kitap in self.kitaplar:
            raise Exception("Bu kitap kütüphanede mevcut")
        else:
            self.kitaplar.append(kitap)
            print("Kitap başarıyla eklendi")
    def kitap_sil(self,kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            print("Kitap başarıyla silindi")
        else:
            raise Exception("Bu kitap kütüphanede mevcut değil")
    def kitaplari_goster(self):
       print("Kitaplar:")
       for kitap in self.kitaplar:
            print(kitap.kitap_adi,kitap.yazar,kitap.sayfa_sayisi,kitap.isbn)

k1=Kitap("açlık oyunları","suzanne collins",320,123456)
k2=Kitap("açlık oyunları2","suzanne collins2",320,123456)
k3=Kitap("açlık oyunları3","suzanne collins3",320,123456)
lib = Kutuphane([k1,k2])
lib.kitaplari_goster()
lib.kitap_sil(k2)
lib.kitaplari_goster()
lib.kitap_ekle(k3)
lib.kitaplari_goster()