# SSA Metodolojisi: Teknik Veriden Hukuki Kanıta

"Üç Katmanlı Savunma Kalkanı" modelimizin kalbinde yer alan teknik veri işleme ve hukuki delillendirme süreci aşağıda detaylandırılmıştır.

## 1. Veri Kaynakları (Data Inputs)
- **TLE (Two-Line Element):** Yörüngedeki nesnelerin konum verileri.
- **RF Monitoring:** Yer istasyonlarından gelen sinyal gücü ve SNR verileri.
- **Katalog Verileri:** BM ve ITU nezdindeki tescil veritabanları.

## 2. İzleme ve Algılama Algoritması
Sistem, belirlenen milli varlıklar (Varlık Seti A) etrafında sanal bir "Hukuki Koruma Küresi" (Legal Protection Sphere) oluşturur.
- **Kritik Mesafe (d < 5km):** Çarpışma riski (CDM) uyarısı üretilir.
- **Sinyal Girişimi (SNR < Threshold):** Jamming tespiti yapılır.

## 3. Hukuki Eşleştirme (Legal Mapping)
Bir anomali tespit edildiğinde, sistem otomatik olarak şu sorguyu yapar:
```sql
SELECT treaty_article 
FROM international_law_db 
WHERE violation_type = 'orbit_infringement' 
AND actor_country = [detected_satellite_owner];
```

## 4. Akıllı Raporlama
Tespit edilen ihlal, **Blockchain** tabanlı bir zaman damgasıyla imzalanarak "Değiştirilemez Delil Paketi" haline getirilir. Bu paket şunları içerir:
- Olay anındaki TLE verileri.
- Sinyal spektrum analizleri.
- İlgili uluslararası madde atıfları.

---
*Bu metodoloji, teknolojinin hukukun hizmetinde nasıl kullanılabileceğini göstermektedir.*
