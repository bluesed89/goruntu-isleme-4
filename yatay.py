import cv2
import numpy as np

# 1. Resmi oku (Türkçe karakter sorununu önleyen güvenli okuma yöntemi)
dosya_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\sadece_gauss.jpg'

try:
    resim_data = np.fromfile(dosya_yolu, dtype=np.uint8)
    resim = cv2.imdecode(resim_data, cv2.IMREAD_GRAYSCALE)
except Exception as e:
    resim = None

if resim is None:
    print("Hata: Resim okunamadı! Yolun ve dosya adının doğru olduğundan emin olun.")
else:
    # 2. YATAY kenarları bulan 3x3'lük yeni filtre (Kernel)
    yatay_filtre = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ], dtype=np.float32)

    # 3. Filtreyi resim üzerinde gezdir (Konvolüsyon)
    yatay_kenarlar = cv2.filter2D(resim, ddepth=-1, kernel=yatay_filtre)

    # 4. Çıktıyı 'yatay_cikti.jpg' olarak kaydet
    cikti_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\yatay_cikti2.jpg'
    is_success, im_buf_arr = cv2.imencode(".jpg", yatay_kenarlar)
    im_buf_arr.tofile(cikti_yolu)
    
    print("İşlem başarılı! Yatay kenar sonucu 'yatay_cikti2.jpg' olarak kaydedildi.")