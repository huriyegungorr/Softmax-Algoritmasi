import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Softmax fonksiyonu
    return exp_x / exp_x.sum()

# Mahalleler ve sentetik kriter değerleri
mahalleler = {
    "Karakaş Mahallesi": [16500, 5, 80000, 4, 7],  # Nüfus, Ulaşım, Maliyet, Çevresel Etki, Sosyal Fayda
    "Cumhuriyet Mahallesi": [3539, 1, 100000, 1, 1],
    "İstasyon Mahallesi": [10111, 2, 30000, 3, 4]
}

# Ağırlıkları belirleme ( Etkilerine göre örn:Maliyet ve çevresel etki negatif etkili)
ağırlıklar = np.array([0.4, 0.2, -0.3, -0.1, 0.3])

def uygun_guzergah_belirle(mahalleler, ağırlıklar):
    mahalle_isimleri = list(mahalleler.keys())
    kriter_degerleri = np.array(list(mahalleler.values()))  
    
    # Softmax'in her kriter için uygulanması
    normal_kriterler = np.apply_along_axis(softmax, 0, kriter_degerleri)
    
    # Ağırlıklıklarla kriterler çarpılarak skorların hesaplanması
    skorlar = np.dot(normal_kriterler, ağırlıklar)
    
    # Sonuçları sözlük formatı şeklinde birleştirilmesi
    skor_dict = {mahalle: skor for mahalle, skor in zip(mahalle_isimleri, skorlar)}
    
    # En iyi mahallenin max skor a göre seçilmesi
    en_uygun = max(skor_dict, key=skor_dict.get)
    
    return en_uygun, skor_dict

en_uygun_mahalle, skorlar = uygun_guzergah_belirle(mahalleler, ağırlıklar)

# Sonuçların mahalle skorlar gezilerek yazdırılması
print("Mahalle Skorları:")
for mahalle, skor in skorlar.items():
    print(f"{mahalle}: {skor:.4f}")

print(f"\nEn uygun güzergah: {en_uygun_mahalle}")
