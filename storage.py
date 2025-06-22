# storage.py
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_user_messages(message):
    user_id = message.from_user.id
    username = message.from_user.username
    message_text = message.text
    now = datetime.now()
    time_string = now.strftime("%H.%M")

    filename = f"USER_{user_id}.json"
    if username:
        filename = f"NICKNAME_{username}.json"

    message_data = {
        "Time": time_string,
        "Message": message_text
    }

    try:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = {
                "ID": user_id,
                "Username": username,
                "First_name": message.from_user.first_name,
                "Messages": []
            }

        if "Messages" not in existing_data:
            existing_data["Messages"] = []

        existing_data["Messages"].append(message_data)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)
        logging.info(f"Message recorded for user {user_id} (file: {filename})")

    except Exception as e:
        logging.error(f"Error writing to file: {e}")