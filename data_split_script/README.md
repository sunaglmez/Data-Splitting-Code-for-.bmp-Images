# Veri Bölme Kodu Kullanım Kılavuzu

Bu Python betiği, .bmp formatındaki görüntü dosyalarını belirtilen oranlarda eğitim (train), doğrulama (validation) ve test setlerine rastgele böler.

## Özellikler

- Belirtilen oranlarda veri bölme (Train: ≈64.87%, Validation: ≈15.62%, Test: ≈19.51%)
- Rastgele seçim ile dosyaların karıştırılması
- Dosyaları kopyalama (orijinal dosyalar korunur)
- Ayrı klasörlere çıktı alma (train, validation, test)
- 1075 adet .bmp formatındaki görüntü için optimize edilmiş

## Kullanım

Betiği komut satırından aşağıdaki parametrelerle çalıştırabilirsiniz:

```bash
python data_splitter.py --source KAYNAK_KLASÖR --output ÇIKTI_KLASÖR
```

### Parametreler

- `--source`: Görüntü dosyalarının bulunduğu kaynak klasör (zorunlu)
- `--output`: Bölünmüş veri setlerinin kaydedileceği çıktı klasörü (zorunlu)
- `--train`: Eğitim seti için oran (varsayılan: 0.6487)
- `--val`: Doğrulama seti için oran (varsayılan: 0.1562)
- `--test`: Test seti için oran (varsayılan: 0.1951)
- `--ext`: Dosya uzantısı filtresi (varsayılan: .bmp)

### Örnek Kullanım

```bash
python data_splitter.py --source /path/to/images --output /path/to/output
```

## Doğrulama Sonuçları

1075 adet görüntü için beklenen sonuçlar:
- Eğitim seti: 697 görüntü (≈64.84%)
- Doğrulama seti: 168 görüntü (≈15.63%)
- Test seti: 210 görüntü (≈19.53%)

## Notlar

- Betik, görüntüleri rastgele karıştırır, bu nedenle her çalıştırmada farklı bir bölme elde edilebilir.
- Oranlar tam olarak sağlanamayabilir çünkü görüntü sayısı tam bölünemeyebilir, ancak mümkün olan en yakın dağılım sağlanır.
