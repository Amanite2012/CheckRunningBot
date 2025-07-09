# Import discord.py
import asyncio
import random
# Send msg
import json, requests
# Secrets
import os
import requests_cache
# Objective calculate optimal conditions to go for a run

# Input: list of tuples (time, rain, temperature, humidity)
# Output dictionnary for recommandations
def build_reco(list_tuple):
    ret = {"01 h": None, "04h": None, "07h": None, "10h": None, "13h": None, "16h": None, "19h": None, "22h": None}
    return ret


def send_message(dataframe):
    for i in range(0, len(dataframe), 3):
        latest_row = dataframe.iloc[i]
        message = (
        f"**Weather Update**\n"
        f"Time (UTC): {latest_row['date']}\n"
        f"Temperature: {latest_row['temperature_2m']}°C\n"
        f"Humidity: {latest_row['relative_humidity_2m']}%\n"
        f"Rain: {latest_row['rain']} mm\n"
        f"Cloud Cover: {latest_row['cloud_cover']}%\n"
        
        )

    # Discord webhook URL
    webhook_url = os.getenv("WEBHOOK_DISCORD")

    # Send the message
    payload = {
      "content": message
    } 
    response = requests.post(webhook_url, json=payload)

  # Check for success
    if response.status_code == 204:
      print("Message sent successfully!")
    else:
      print(f"Failed to send message: {response.status_code} - {response.text}")
