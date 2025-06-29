import requests
import json
import logging

def load_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("config.json not found. Please create it.")
        return {}
    except json.JSONDecodeError:
        logging.error("Error decoding config.json. Please check its format.")
        return {}

def send_message(text):
    cfg = load_config()
    token = cfg.get("telegram_token")
    chat_id = cfg.get("telegram_chat_id")

    if not token or not chat_id:
        logging.error("Telegram token or chat ID not configured in config.json.")
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        logging.info(f"Telegram message sent: {text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Telegram send_message error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred in send_message: {e}")

def send_file(filepath, caption=""):
    cfg = load_config()
    token = cfg.get("telegram_token")
    chat_id = cfg.get("telegram_chat_id")

    if not token or not chat_id:
        logging.error("Telegram token or chat ID not configured in config.json.")
        return

    url = f"https://api.telegram.org/bot{token}/sendDocument"
    try:
        with open(filepath, "rb") as f:
            files = {"document": f}
            data = {"chat_id": chat_id, "caption": caption}
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            logging.info(f"Telegram file sent: {filepath}")
    except FileNotFoundError:
        logging.error(f"File not found for Telegram: {filepath}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Telegram send_file error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred in send_file: {e}")