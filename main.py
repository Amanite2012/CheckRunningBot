import call_api.meteo as meteo
import marketing.graph as graph
import marketing.discord_ex as discord_ex

# Setup the Open-Meteo API client with cache and retry on error
dataframe = meteo.get_meteo_pd()
# Send the message to Discord
discord_ex.send_message(dataframe)
# Build the graph
graph.build_rain_graph(dataframe)
# Send the message to Discord
