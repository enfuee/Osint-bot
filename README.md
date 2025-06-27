# 🔍 OSINT Telegram CLI Bot

Bot terminal untuk melakukan investigasi OSINT dengan alat:
- Sherlock
- Maigret
- theHarvester
- SpiderFoot

Hasil akan dikirim otomatis ke Telegram.

## 📦 Fitur
- Pencarian username di ratusan situs (Sherlock, Maigret)
- Pencarian email & subdomain berdasarkan domain (theHarvester)
- Passive OSINT lengkap (SpiderFoot)
- Pengiriman laporan otomatis ke Telegram

## 🚀 Instalasi
```bash
git clone https://github.com/kamu/osint-telegram-bot.git
cd osint-telegram-bot
chmod +x installer.sh
./installer.sh
```

## ⚙️ Konfigurasi
Buat file `config.json` di folder utama:
```json
{
  "telegram_token": "TOKEN_BOT_KAMU",
  "telegram_chat_id": "CHAT_ID_KAMU"
}
```

## ▶️ Penggunaan
```bash
python3 main.py --target naraditya --mode username
python3 main.py --target diskominfo.go.id --mode domain
python3 main.py --target naraditya --mode all
```

## 🗂 Struktur Project
```
osint-telegram-bot/
├── installer.sh
├── requirements.txt
├── config.json
├── main.py
├── modules/
│   ├── sherlock_runner.py
│   ├── maigret_runner.py
│   ├── harvester_runner.py
│   └── spiderfoot_runner.py
├── utils/
│   └── telegram.py
└── reports/
```

## 📤 Output
Semua laporan akan disimpan di folder `reports/` dan dikirim ke Telegram bot kamu.