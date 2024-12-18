# Input: dates[]
# Output: int[] -> Rain

import re
import requests
import pandas as pd
import xml.etree.ElementTree as ET

import os
import dotenv

def build_tuple_time_thermo_humidity_rain(tree):
  ret = []
  for child in tree.findall('echeance'):
    # Temperature 2m from ground
    temperature = child.find('temperature')[0].text
    humidity = child.find('humidite')[0].text
    rain = child.find('pluie').text
    timestamp = child.get('timestamp')
    ret.append((timestamp, temperature, rain, humidity))
  return ret

def get_rain():
  dotenv.load_dotenv()
  
  position_lat = os.getenv("POSITION_LAT")
  position_lon = os.getenv("POSITION_LON")
 
  url = f"http://www.infoclimat.fr/public-api/gfs/xml?_ll={position_lat},{position_lon}&_auth=%3D%3D&_c=9f4d75a8f93f20382a6b14d70475d361"
  print(url)
  url_response = requests.get(url)
  data = url_response.content
  with open('mon_fichier.xml', 'w') as f:

    # Écriture de la chaîne de caractères dans le fichier.
    f.write(data.decode("utf-8"))
  # Parsing tree XML
  # Objective si to get a tree of dates and rain values
  
  tree = ET.parse('mon_fichier.xml')

  root = tree.getroot()
  list_meteo = build_tuple_time_thermo_humidity_rain(root)
  print(list_meteo)
  return list_meteo
