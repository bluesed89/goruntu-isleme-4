import cv2
import numpy as np

dosya_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\resim.jpg'

# Türkçe karakter destekli okuma
try:
    resim_data = np.fromfile(dosya_yolu, dtype=np.uint8)
    resim = cv2.imdecode(resim_data, cv2.IMREAD_GRAYSCALE)
except Exception as e:
    resim = None

if resim is None:
    print("Hata: Resim okunamadı! Dosya adının 'resim.jpg' ve uzantısının doğru olduğundan emin olun.")
else:
    dikey_filtre = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ], dtype=np.float32)

    dikey_kenarlar = cv2.filter2D(resim, ddepth=-1, kernel=dikey_filtre)

    # Türkçe karakter destekli kaydetme
    cikti_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\cikti.jpg'
    is_success, im_buf_arr = cv2.imencode(".jpg", dikey_kenarlar)
    im_buf_arr.tofile(cikti_yolu)
    
    print("İşlem başarılı! Sonuç kaydedildi.")