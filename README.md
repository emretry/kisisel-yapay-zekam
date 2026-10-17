# Kişisel Yapay Zekâm — ilk sürüm

Bu uygulama Streamlit üzerinde çalışır ve Gemini API ile yanıt üretir.

## 1. Hesaplar
- GitHub hesabı: https://github.com/
- Google AI Studio: https://aistudio.google.com/
- Streamlit Community Cloud: https://share.streamlit.io/

## 2. Dosyaları GitHub'a koy
1. GitHub'da `kisisel-yapay-zekam` adlı yeni bir repository oluştur.
2. İlk denemede repository public olabilir; bu durumda kodun herkese açık olabileceğini unutma.
3. `app.py` ve `requirements.txt` dosyalarını yükle. API anahtarını hiçbir zaman dosyalara yazma.

## 3. Gemini API anahtarı
1. Google AI Studio'da API key oluştur.
2. Anahtarı kimseyle paylaşma ve GitHub'a koyma.

## 4. Streamlit'te yayımla
1. https://share.streamlit.io/ adresini aç ve GitHub ile giriş yap.
2. Create app seç.
3. Repository olarak `kisisel-yapay-zekam`, dosya olarak `app.py` seç ve Deploy'a bas.
4. Uygulama ayarlarında Secrets bölümüne aşağıdakileri kendi değerlerinle ekle:

APP_PASSWORD = "buraya_uzun_ve_tahmin_edilmesi_zor_bir_sifre"
GOOGLE_API_KEY = "Google_AI_Studio_API_anahtarin"

5. Kaydet ve uygulamayı yeniden başlat.

## Güvenlik notları
- Ücretsiz Streamlit dağıtımında uygulama URL'si başkaları tarafından bulunabilir. Bu örnek basit bir şifre kapısı içerir ama profesyonel kimlik doğrulama değildir.
- Hassas veya özel bilgileri ilk sürüme koyma.
- API anahtarını asla kaynak koda veya herkese açık GitHub deposuna ekleme.
- Gemini model adları, erişim ve ücretsiz kotalar değişebilir. Model hatası alırsan AI Studio hesabındaki kullanılabilir modelleri kontrol et.
- Bu sürüm sohbet geçmişini kalıcı olarak kaydetmez; oturum kapanınca geçmiş kaybolabilir.
