import cv2
import numpy as np

dosya_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\resim.jpg'

try:
    resim_data = np.fromfile(dosya_yolu, dtype=np.uint8)
    resim = cv2.imdecode(resim_data, cv2.IMREAD_GRAYSCALE)
except Exception as e:
    resim = None

if resim is None:
    print("Hata: Resim okunamadı!")
else:
    # ÇAPRAZ Filtre Matrisi (Sol Üst -> Sağ Alt)
    capraz_filtre = np.array([
        [-2, -1,  0],
        [-1,  0,  1],
        [ 0,  1,  2]
    ], dtype=np.float32)

    # Filtreyi gezdir
    capraz_kenarlar = cv2.filter2D(resim, ddepth=-1, kernel=capraz_filtre)

    # Kaydet
    cikti_yolu = r'C:\Users\Casper\Desktop\görüntü işleme\4.hafta\capraz_cikti.jpg'
    is_success, im_buf_arr = cv2.imencode(".jpg", capraz_kenarlar)
    im_buf_arr.tofile(cikti_yolu)
    
    print("İşlem başarılı! Çapraz kenar sonucu 'capraz_cikti.jpg' olarak kaydedildi.")