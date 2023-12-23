# Input: dates[]
# Output: int[] -> Rain

import dotenv
import re
import requests
import pandas as pd
import xml.etree.ElementTree as ET

def is_valid_date(date_string):
  pattern = r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}"
  match = re.match(pattern, date_string)
  return match is not None

import os
import requests
import dotenv

def list_tree(tree):
  ret = []
  for child in tree:
    if child.tag == "echeance":
      ret.append(child)
  return ret

def get_rain():
  dotenv.load_dotenv()
  
  position_lat = os.getenv("POSITION_LAT")
  position_lon = os.getenv("POSITION_LON")
 
  url = f"http://www.infoclimat.fr/public-api/gfs/xml?_ll={position_lat},{position_lon}&_auth=CRNRRgZ4VXdVeAE2UiRVfFY%2BVGEKfAYhBXkAYwlsUi9ROlEwVDQAZgNtAH1SfQs9Un9VNg41BTVUP1EpWCpXNgljUT0GbVUyVToBZFJ9VX5WeFQ1CioGIQVnAG4JYVIvUTNRNlQ1AHwDbQBkUmALIVJpVSoOLgU8VDBRNlg0VzIJaFEzBmVVN1U%2FAXxSfVVnVmBUMgpmBm0FZgBuCWFSMlE3UWFUMwBiA28AfFJlCzlSaFUzDjAFNVQ1UT5YKlcrCRNRRgZ4VXdVeAE2UiRVfFYwVGoKYQ%3D%3D&_c=b60bcb11da3d5217338f5960bdd2180a"

  url_response = requests.get(url)
  data = url_response.content
  with open('mon_fichier.xml', 'w') as f:

    # Écriture de la chaîne de caractères dans le fichier.
    f.write(data.decode("utf-8"))
  # Parsing tree XML
  # Objective si to get a tree of dates and rain values
  tree = ET.parse('mon_fichier.xml')

  root = tree.getroot()
  list_tree(root)
  
  return 0
