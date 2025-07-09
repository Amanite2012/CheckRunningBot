# Import discord.py
import asyncio
import random
# Send msg
import json, requests
# Secrets
import os
import dotenv # Added dotenv
import requests_cache

dotenv.load_dotenv() # Load .env file

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


def send_image_to_discord(image_path: str, message: str = "Meteorological Graph"):
    """
    Sends an image file to a Discord webhook.

    Args:
        image_path (str): The path to the image file.
        message (str, optional): The message content to send with the image. Defaults to "Meteorological Graph".
    """
    webhook_url = os.getenv("WEBHOOK_DISCORD")
    if not webhook_url:
        print("Error: WEBHOOK_DISCORD environment variable not set.")
        return

    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return

    try:
        with open(image_path, 'rb') as f:
            files = {'file': (os.path.basename(image_path), f)}
            payload = {"content": message}
            response = requests.post(webhook_url, data=payload, files=files)

        if response.status_code == 200 or response.status_code == 204: # Discord API can return 200 for file uploads
            print(f"Image '{image_path}' sent successfully to Discord!")
        else:
            print(f"Failed to send image to Discord: {response.status_code} - {response.text}")
            try:
                print(f"Response content: {response.json()}")
            except requests.exceptions.JSONDecodeError:
                print("Response content is not JSON.")

    except FileNotFoundError:
        print(f"Error: Could not find the image file at {image_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending image to Discord: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
