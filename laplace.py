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
    # 2. ADIM: Gauss ile Hafif Yumuşatma
    gauss_resim = cv2.GaussianBlur(resim, (3, 3), 0)

    # 3. ADIM: 3x3 Laplacian Çekirdeğinin Tanımlanması
    laplacian_kernel = np.array([
        [0,  1, 0],
        [1, -4, 1],
        [0,  1, 0]
    ], dtype=np.float32)

    # 4. ADIM: Filtreyi Gezdirme (Konvolüsyon)
    laplacian_kenarlar = cv2.filter2D(gauss_resim, ddepth=-1, kernel=laplacian_kernel)

    # 5. ADIM: Sonucu Kaydetme
    cikti_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\laplacian_cikti.jpg'
    is_success, im_buf_arr = cv2.imencode(".jpg", laplacian_kenarlar)
    im_buf_arr.tofile(cikti_yolu)
    
    print("İşlem başarılı! Gauss + Laplacian sonucu 'laplacian_cikti.jpg' olarak kaydedildi.")