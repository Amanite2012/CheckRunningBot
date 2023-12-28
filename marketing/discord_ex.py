# Import discord.py
import asyncio
import random
# Send msg
import json, requests
# Secrets
import os, dotenv

# Objective calculate optimal conditions to go for a run

def send_message():
    dotenv.load_dotenv()
    webhook_url = os.getenv("WEBHOOK_DISCORD")
    print(webhook_url)
    data = {
    "content": "Bonjour et bienvuenue pour les prévisions de la semaine TODO.\nVoici les prévisions:\n**Lundi**: TODO\n**Mardi**: TODO",
    "embeds": [
      {
        "title": "Méthodes de suggestion",
        "description": "Il s'avère que la température pour maximiser les performances est de 9 de degrés pour les femmes et de 6 degrés pour les hommes (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037407#pone-0037407-g004). Cette température a tendance a diminuer avec l'augmentation des capacités physiques.\n\nQuant à la pollution, nous nous sommes intéressés à l'impact sur les performances immédiates. Il s'avère que courir avec une pollution (AQI) de + de 100 équivaut à une augmentation au temps de +4%. (https://www.lung.org/blog/running-outside-air-pollution)\nC'est pourquoi nous vous déconseillerons toujours les périodes de fortes pollution.",
        "author": {
          "name": "Par Amanite"
        }
      }
    ],
    "username": "Running bot",
    "attachments": []
  }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        print("Message sent successfully")
    else:
        print("Error sending message:", response.status_code)
