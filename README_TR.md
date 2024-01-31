
# TCDD Bilet Bulucu

## Genel Bakış

TCDD Tren Koltuk Bulucu, kullanıcıların Türkiye Cumhuriyeti Devlet Demiryolları (TCDD) trenlerinde boş koltuk bulmasına yardımcı olan Python tabanlı bir araçtır. Belirli güzergahlar, tarihler ve isteğe bağlı olarak saatler için koltuk müsaitliğini kontrol etme işlemini otomatikleştirir. Müsait bir koltuk bulunduğunda, araç kullanıcıyı e-posta yoluyla bilgilendirir ve tren adı, yolculuk tarihi, vagon numarası ve koltuk numarası gibi detayları sağlar.

## Özellikler
- **Otomatik Koltuk Kontrolü**: Belirtilen tren güzergahlarında müsait koltukları otomatik olarak kontrol eder.
- **E-posta Bildirimleri**: Müsait koltuklar bulunduğunda detaylı bilgilerle e-posta uyarıları gönderir.
- **Yapılandırılabilir Aramalar**: Kalkış ve varış istasyonlarını, yolculuk tarihlerini ve isteğe bağlı olarak tercih edilen kalkış saatlerini belirleyebilirsiniz.

## Kurulum

### Gereksinimler
- Python 3.x
- Pip (Python paket yükleyicisi)

### Kurulum Adımları
1. Depoyu yerel makinenize klonlayın:
   ```sh
   git clone https://github.com/rburaksaritas/tcdd-bilet-bulucu
   ```
2. Proje dizinine gidin:
   ```sh
   cd tcdd-bilet-bulucu
   ```
3. Gerekli bağımlılıkları yükleyin:
   ```sh
   pip3 install -r requirements.txt
   ```

## Yapılandırma
Araçları kullanmadan önce, `src` dizininde bulunan `config.py` dosyasını düzenleyerek yapılandırmanız gerekir. Aşağıdaki parametreleri tercihlerinize göre ayarlayın:

- `binis_istasyon_adi`: Kalkış istasyonunun adı.
- `inis_istasyon_adi`: Varış istasyonunun adı.
- `date`: Yolculuk tarihi (format: YYYY-AA-GG).
- `check_specific_hour`: Belirli bir saatte trenleri kontrol etmek istiyorsanız `True` olarak ayarlayın, aksi takdirde `False`.
- `hour`: Tercih edilen kalkış saati (format: SS:DD), `check_specific_hour` `True` ise gereklidir.
- `email_address`: Bildirimin gönderileceği e-posta adresiniz.
- `email_password`: Yukarıdaki e-posta hesabının şifresi.
- `destination_address`: Bildirimi alacak e-posta adresi.

**Not:** `binis_istasyon_adi` ve `inis_istasyon_adi` geçerli istasyon adları olmalıdır. Mevcut istasyon adları için `stations.json` dosyasına bakınız.

## Kullanım
Bilet bulucuyu başlatmak için `main.py` dosyasını çalıştırın:
```sh
python3 main.py
```

Araç, belirtilen yapılandırmaya göre periyodik olarak müsait koltukları kontrol edecek ve bir koltuk bulunduğunda e-posta ile bildirim gönderecektir.

## Sorumluluk Reddi Beyanı
Bu araç yalnızca eğitimsel amaçlar içindir ve kesinlikle TCDD ile hiçbir ilişiği bulunmamaktadır. Lütfen sorumlu bir şekilde ve TCDD'nin hizmet şartlarına uygun olarak kullanın.
