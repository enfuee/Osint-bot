#!/bin/bash

# OSINT Toolkit Installer

set -e

echo "[+] Memperbarui sistem..."
sudo apt update && sudo apt install -y git python3 python3-pip curl

mkdir -p osint-tools && cd osint-tools

# Install Sherlock
echo "[+] Mengkloning Sherlock..."
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
pip3 install -r requirements.txt
cd ..

# Install Maigret
echo "[+] Mengkloning Maigret..."
git clone https://github.com/soxoj/maigret.git
cd maigret
pip3 install -r requirements.txt
cd ..

# Install theHarvester
echo "[+] Mengkloning theHarvester..."
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
pip3 install -r requirements/base.txt
cd ..

# Install SpiderFoot (CLI Mode)
echo "[+] Mengkloning SpiderFoot..."
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot
pip3 install -r requirements.txt
cd ..

# Kembali ke root dan setup bot
cd ..
echo "[+] Membuat virtualenv untuk bot..."
pip3 install -r requirements.txt || true

mkdir -p reports

echo "[✓] Semua tools OSINT telah terinstall!"
echo "Jalankan: python3 main.py --target [nama] --mode all"
