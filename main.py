import call_api.rain as rain
import marketing.graph as graph


list_time_rain = rain.get_rain()
graph.build_rain_graph(list_time_rain)