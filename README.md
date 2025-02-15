# Softmax-Algoritmasi 
Proje Tanımı:  

Bu proje Kırklareli'nde bulunan 3 mahalle için yeni bir toplu taşıma hattı planlaması yapmak amaçlanmıştır. Projede softmax algoritmasından yararlanılmıştır.Nüfus yoğunluğu, ulaşım altyapısı, maliyet analizi, çevresel etki ve sosyal fayda gibi kriterler değerlendirilmiştir.  

Projede kullanılan yöntemler:  
Projede softmax algoritmasından yararlanılarak kriterlerin normalizasyonu sağlanmış ve mahallelerin ağırlıklandırılmış skorları hesaplanmıştır.   

Proje Adımları:  
Verilerin Oluşturulması: Bilinen veriler doğru bir şekilde bazıları tahmine dayalı olarak kriterlere değerler atanmıştır.  
Verilerin Normalizasyonu: Veriler softmax ile normalize edilmiş olup veriler arasındaki farklı birimlerin yarattığı dengesizlikler ortadan kaldırıldı.  
Skorların Hesaplanması: Her kritere belirli bir ağırlık verilerek her mahalle için toplam skor hesaplandı.  
En Uygun Mahallenin Belirlenmesi: Mahallelerin skorları karşılaştırılarak en uygun mahalle belirlendi.  
Kurulum ve Kullanım:  
Bu projeyi çalıştırabilmek için gereken gereksinimler python ve numphy kütüphanesine sahip olunması ve bunların çalışacağı ortamın bulunması gereklidir.  
Bu kod dosyasının kullanılabilinmesi için bu repoyu code butonuna tıklanarak download seçeneği ile indirebilir, eğer Git yüklüyse terminalde git clone <repo link> komutu ile kod klonlanabilir.   
Proje Çıktıları:
Mahalle Skorları:
Karakaş Mahallesi: -0.3000
Cumhuriyet Mahallesi: -0.3000
İstasyon Mahallesi: -0.3000

En uygun güzergah: Karakaş Mahallesi  
Projede bazı verilerin birbirine yakın olması sebebi ile softmax ile normalizasyon yaptıktan sonra elde edilen sonuçlar çok benzer olabilir, bu da skorların benzer çıkmasına neden olacaktır.






