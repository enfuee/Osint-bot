#!/bin/bash

# OSINT Toolkit Installer
set -e

GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RESET=$(tput sgr0)

# === KONFIGURASI TELEGRAM ===
TELEGRAM_TOKEN="7855485986:AAET98uOgVKsIK0SGRxnef4xZi3UZmywQ4Y"  # GANTI jika perlu
CHAT_ID="7283938561"  # GANTI dengan ID chatmu

send_telegram() {
  curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_TOKEN/sendMessage" \
       -d chat_id="$CHAT_ID" \
       -d parse_mode="Markdown" \
       -d text="$1"
}

echo "${GREEN}[+] Memperbarui sistem dan menginstal dependensi...${RESET}"
sudo apt update
sudo apt install -y git python3 python3-pip curl

echo "${GREEN}[+] Membuat folder osint-tools...${RESET}"
mkdir -p osint-tools
cd osint-tools

# Install Sherlock
if [ ! -d "sherlock" ]; then
  echo "${GREEN}[+] Mengkloning Sherlock...${RESET}"
  git clone https://github.com/sherlock-project/sherlock.git
  cd sherlock
  pip3 install -r requirements.txt
  cd ..
else
  echo "${YELLOW}[=] Sherlock sudah ada, lewati...${RESET}"
fi

# Install Maigret
if [ ! -d "maigret" ]; then
  echo "${GREEN}[+] Mengkloning Maigret...${RESET}"
  git clone https://github.com/soxoj/maigret.git
  cd maigret
  pip3 install -r requirements.txt
  cd ..
else
  echo "${YELLOW}[=] Maigret sudah ada, lewati...${RESET}"
fi

# Install theHarvester
if [ ! -d "theHarvester" ]; then
  echo "${GREEN}[+] Mengkloning theHarvester...${RESET}"
  git clone https://github.com/laramies/theHarvester.git
  cd theHarvester
  pip3 install -r requirements/base.txt
  cd ..
else
  echo "${YELLOW}[=] theHarvester sudah ada, lewati...${RESET}"
fi

# Install SpiderFoot
if [ ! -d "spiderfoot" ]; then
  echo "${GREEN}[+] Mengkloning SpiderFoot...${RESET}"
  git clone https://github.com/smicallef/spiderfoot.git
  cd spiderfoot
  pip3 install -r requirements.txt
  cd ..
else
  echo "${YELLOW}[=] SpiderFoot sudah ada, lewati...${RESET}"
fi

# Kembali ke root project
cd ..

echo "${GREEN}[+] Membuat folder laporan...${RESET}"
mkdir -p reports

echo "${GREEN}[+] Menginstal dependensi Python bot...${RESET}"
pip3 install -r requirements.txt || true

echo "${GREEN}[✓] Semua tools OSINT berhasil diinstal!${RESET}"
echo ""
echo "${YELLOW}🔧 Gunakan perintah berikut untuk menjalankan bot:${RESET}"
echo "    python3 main.py --target [username/domain] --mode [username|domain|all]"

# === KIRIM NOTIFIKASI ===
send_telegram "✅ *Installer OSINT Bot Selesai*\nSemua tool berhasil diinstal.\n\nGunakan:\n\`python3 main.py --target [nama] --mode all\`"
