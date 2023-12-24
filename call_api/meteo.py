# Input: dates[]
# Output: int[] -> Rain

import dotenv
import re
import requests
import pandas as pd
import xml.etree.ElementTree as ET

import os
import requests
import dotenv

def build_tuple_time_rain(tree):
  ret = []
  for child in tree.findall('echeance'):
    # Temperature 2m from ground
    temperature = child.find('temperature')[0].text
    timestamp = child.get('timestamp')
    ret.append((timestamp, temperature))
  return ret

def get_rain():
  dotenv.load_dotenv()
  
  position_lat = os.getenv("POSITION_LAT")
  position_lon = os.getenv("POSITION_LON")
 
  url = f"http://www.infoclimat.fr/public-api/gfs/xml?_ll={position_lat},{position_lon}&_auth=BhwEE1UrU3FWe1ZhAHYFLFI6UmcNe1VyBXkHZF86VyoEb1U0BmYDZQBuWidXeAcxWHUPbA02V2cLYFUtXS9RMAZsBGhVPlM0VjlWMwAvBS5SfFIzDS1VcgVvB2JfLFc1BG9VNQZ7A2AAblo6V3kHMFhoD3ANLVduC29VMl0zUTYGZgRmVT9TMVY6VisALwU3UmRSOg06VWsFZAdmXzVXNgRlVTQGYQMwAGxaJldnBzpYYg9oDTNXbAtsVTddL1EtBhwEE1UrU3FWe1ZhAHYFLFI0UmwNZg%3D%3D&_c=9f4d75a8f93f20382a6b14d70475d361"
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
  list_time_rain = build_tuple_time_rain(root)
  
  return list_time_rain
