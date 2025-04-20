import call_api.meteo as meteo
import marketing.graph as graph
import marketing.discord_ex as discord_ex

#list_time_rain = meteo.get_rain()
#graph.build_rain_graph(list_time_rain)
#discord_ex.send_message()


import openmeteo_requests
import pandas as pd
from retry_requests import retry
import requests

# Setup the Open-Meteo API client with cache and retry on error
dataframe = meteo.get_meteo_pd()
# Send the message to Discord
discord_ex.send_message(dataframe)
# Build the graph
graph.build_rain_graph(dataframe)
# Send the message to Discord