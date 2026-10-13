import cv2
import numpy as np

dosya_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\resim.jpg'

# 1. Türkçe karakter destekli resim okuma (Siyah-Beyaz)
try:
    resim_data = np.fromfile(dosya_yolu, dtype=np.uint8)
    resim = cv2.imdecode(resim_data, cv2.IMREAD_GRAYSCALE)
except Exception as e:
    resim = None

if resim is None:
    print("Hata: Resim okunamadı! Yolun doğru olduğundan emin olun.")
else:
    # 2. Sadece Gauss Bulanıklaştırması Uygula
    # (5, 5) -> Çekirdek (filtre) boyutu (Bulanıklık miktarını artırmak için 7x7 veya 9x9 yapabilirsin)
    # 0 -> Otomatik standart sapma
    gauss_resim = cv2.GaussianBlur(resim, (5, 5), 0)

    # 3. Sonucu 'sadece_gauss.jpg' olarak kaydet
    cikti_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\sadece_gauss.jpg'
    is_success, im_buf_arr = cv2.imencode(".jpg", gauss_resim)
    im_buf_arr.tofile(cikti_yolu)
    
    print("İşlem başarılı! Sadece Gauss uygulanmış resim 'sadece_gauss.jpg' olarak kaydedildi.")