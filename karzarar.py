import time
import random

kar = 0

baslangic_fiyati_altin = 450

para = 1000

karli_para = 1000

altin_miktari = para / baslangic_fiyati_altin

hesap_cuzdani = 0

kar_miktari = 0

icon = ["","","-"]
while True:
    time.sleep(0.5)
    updown = round(random.random(), 4)
    ico = random.choice(icon)
    kur_hareketi = ico + str(updown)
    toplam_kur_hareketi = float(kur_hareketi) + baslangic_fiyati_altin
    alis_kuru = float(kur_hareketi) + toplam_kur_hareketi
        
    para = altin_miktari * alis_kuru
    
    if para > 1004:
        kar = para - 1000
        karli_para = kar + karli_para
        kar_miktari += kar
        print("----------------")
        print("Elde edilen kar: ", round(kar,3))
        print("Toplam para    : ", round(karli_para,3))
        if kar_miktari > 100:
            print("HESABA PARA YÜKLENİYOR")
            for i in range(5):
                print(end=".")
                time.sleep(1)
            hesap_cuzdani += kar_miktari
            kar_miktari = 0
            karli_para = karli_para - 100
            print("Hesap Cüzdanı : ", hesap_cuzdani)
            
    elif para < 1002:
        print("------------------------")
        print("Hiçbir İşlem Yapılmadı : ", round(para,3))
        
    
    
    
