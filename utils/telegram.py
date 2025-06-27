import requests
import json

def load_config():
    with open("config.json") as f:
        return json.load(f)

def send_message(text):
    cfg = load_config()
    token = cfg["telegram_token"]
    chat_id = cfg["telegram_chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

def send_file(filepath, caption=""):
    cfg = load_config()
    token = cfg["telegram_token"]
    chat_id = cfg["telegram_chat_id"]
    url = f"https://api.telegram.org/bot{token}/sendDocument"
    with open(filepath, "rb") as f:
        files = {"document": f}
        data = {"chat_id": chat_id, "caption": caption}
        requests.post(url, data=data, files=files)
