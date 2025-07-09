
import openmeteo_requests
import pandas as pd
import xml.etree.ElementTree as ET
from retry_requests import retry
import os,dotenv
import requests_cache


def get_meteo_pd():
  dotenv.load_dotenv()
  cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
  retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
  openmeteo = openmeteo_requests.Client(session = retry_session)
  url = "https://api.open-meteo.com/v1/forecast"

  lat = os.getenv("LATITUDE")
  lon = os.getenv("LONGITUDE")

  params = {
    "latitude": lat,
    "longitude": lon,
    "hourly": ["temperature_2m", "relative_humidity_2m", "rain", "cloud_cover"]
  }
  
  responses = openmeteo.weather_api(url, params=params)

  # Process first location. Add a for-loop for multiple locations or weather models
  response = responses[0]
  print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
  print(f"Elevation {response.Elevation()} m asl")
  print(f"Timezone {response.Timezone()}{response.TimezoneAbbreviation()}")
  print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

  # Process hourly data. The order of variables needs to be the same as requested.
  hourly = response.Hourly()
  hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

  hourly_data = {"date": pd.date_range(
    start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
    end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
    freq = pd.Timedelta(seconds = hourly.Interval()),
    inclusive = "left"
  )}

  hourly_data["temperature_2m"] = hourly_temperature_2m
  hourly_data["relative_humidity_2m"] = hourly.Variables(1).ValuesAsNumpy()
  hourly_data["rain"] = hourly.Variables(2).ValuesAsNumpy()
  hourly_data["cloud_cover"] = hourly.Variables(3).ValuesAsNumpy()

  hourly_dataframe = pd.DataFrame(data = hourly_data)
  
  return hourly_dataframe