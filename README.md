# Telegram Futbol Analiz Botu

Bu proje, Telegram üstünden SportMonks verisi kullanarak:
- bugünün maçlarını listeleyen
- canlı maçları gösteren
- fixture id ile maç analizi veren
- basit tahmin/istatistik çıktısı üreten
bir başlangıç botudur.

## 1) Kurulum

```bash
pip install -r requirements.txt
cp .env.example .env
```

`.env` içine kendi tokenlarını yaz:

```env
TELEGRAM_BOT_TOKEN=senin_telegram_bot_token
SPORTMONKS_API_TOKEN=senin_sportmonks_token
DEFAULT_TIMEZONE=Europe/Istanbul
DEFAULT_LEAGUE_IDS=8,271,301
```

> `DEFAULT_LEAGUE_IDS` boş kalırsa erişebildiğin tüm liglerden veri çekmeye çalışır.

## 2) Çalıştırma

```bash
python main.py
```

## 3) Telegram komutları

- `/start`
- `/maclar`
- `/canli`
- `/analiz 12345678`
- `/istatistik 12345678`

## 4) Railway kurulumu

Railway Variables kısmına şunları ekle:
- `TELEGRAM_BOT_TOKEN`
- `SPORTMONKS_API_TOKEN`
- `DEFAULT_TIMEZONE`
- `DEFAULT_LEAGUE_IDS`

Start command / Procfile:

```bash
python main.py
```

## 5) Bu sürümde neler hazır?

- Modüler klasör yapısı
- SportMonks API servis katmanı
- Telegram command handler sistemi
- Basit analiz motoru
- Basit tahmin motoru
- Railway için hazır temel yapı

## 6) Sonraki aşamada ne eklenir?

- takım adına göre maç arama
- canlı baskı analizi
- ilk yarı / maç sonu tahminleri
- korner ve kart istatistikleri
- otomatik kanal paylaşımı
- admin panel komutları
- favori lig filtresi
- görsel/şablon mesaj tasarımı
