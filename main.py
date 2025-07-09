import call_api.meteo as meteo
import marketing.graph as graph
import marketing.discord_ex as discord_ex

list_time_rain = meteo.get_rain()
graph.build_rain_graph(list_time_rain)
discord_ex.send_message()
