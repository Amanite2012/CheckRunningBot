# Import discord.py
import asyncio
import random
# Send msg
import json, requests
# Secrets
import os, dotenv

# Objective calculate optimal conditions to go for a run

# Input: list of tuples (time, rain, temperature, humidity)
# Output dictionnary for recommandations
def build_reco(list_tuple):
    ret = {"01 h": None, "04h": None, "07h": None, "10h": None, "13h": None, "16h": None, "19h": None, "22h": None}
    return ret


def send_message():
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_DISCORD")
    message = {"ayoh": ':green_circle:', "test": 3}
    msg = str(message)
    data = {
        "content": msg
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        print("Message sent successfully")
    else:
        print("Error sending message:", response.status_code)
