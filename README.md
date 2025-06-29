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

1. **Kloning Repositori:**
```bash
git clone https://github.com/enfuee/Osint-bot.git
cd Osint-bot
```

2. **Instal Poetry (jika belum ada):**
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/ubuntu/.local/bin:$PATH"
```

3. **Instal Dependensi dengan Poetry:**
```bash
poetry install
```

## ⚙️ Konfigurasi

Buat file `config.json` di folder utama proyek dengan struktur berikut. Pastikan untuk mengganti placeholder dengan nilai yang sesuai dan mengatur jalur ke alat eksternal yang telah Anda instal.

```json
{
  "telegram_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "telegram_chat_id": "YOUR_TELEGRAM_CHAT_ID",
  "tool_paths": {
    "sherlock": "/path/to/your/sherlock/directory",
    "maigret": "/path/to/your/maigret/directory",
    "theharvester": "/path/to/your/theharvester/directory",
    "spiderfoot": "/path/to/your/spiderfoot/directory"
  }
}
```

**Catatan:** Pastikan jalur yang Anda berikan di `tool_paths` adalah direktori tempat skrip utama alat (misalnya, `sherlock.py`, `maigret.py`, `theHarvester.py`, `sf.py`) berada.

## ▶️ Penggunaan

Jalankan bot menggunakan Poetry. Anda dapat menentukan target (username atau domain), mode scan, dan alat spesifik yang ingin dijalankan.

```bash
poetry run python main.py --target naraditya --mode username
poetry run python main.py --target diskominfo.go.id --mode domain
poetry run python main.py --target naraditya --mode all
poetry run python main.py --target naraditya --mode username --tools sherlock maigret
poetry run python main.py --target diskominfo.go.id --mode domain --tools theharvester
```

## 🗂 Struktur Project
```
osint-telegram-bot/
├── poetry.lock
├── pyproject.toml
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

