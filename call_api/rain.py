# Input: dates[]
# Output: int[] -> Rain

import dotenv
import re
import requests
import pandas as pd
import json

def is_valid_date(date_string):
  pattern = r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}"
  match = re.match(pattern, date_string)
  return match is not None

def get_rain():
    dotenv.load_dotenv()  
    url_response= requests.get("http://www.infoclimat.fr/public-api/gfs/xml?_ll="+ env.POSITION_LAT +","+ env.POSITION_LON +"&_auth=CRNRRgZ4VXdVeAE2UiRVfFY%2BVGEKfAYhBXkAYwlsUi9ROlEwVDQAZgNtAH1SfQs9Un9VNg41BTVUP1EpWCpXNgljUT0GbVUyVToBZFJ9VX5WeFQ1CioGIQVnAG4JYVIvUTNRNlQ1AHwDbQBkUmALIVJpVSoOLgU8VDBRNlg0VzIJaFEzBmVVN1U%2FAXxSfVVnVmBUMgpmBm0FZgBuCWFSMlE3UWFUMwBiA28AfFJlCzlSaFUzDjAFNVQ1UT5YKlcrCRNRRgZ4VXdVeAE2UiRVfFYwVGoKYQ%3D%3D&_c=b60bcb11da3d5217338f5960bdd2180a")

    data = response.content
    print(data)
    #dates = []
    #for key in parsed_json:
    #if is_valid_date(key):
    #    dates.append(key)

    return 0