import call_api.meteo as meteo
import marketing.graph as graph


list_time_rain = meteo.get_rain()
graph.build_rain_graph(list_time_rain)