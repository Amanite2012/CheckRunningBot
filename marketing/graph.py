"""
File used to generate graphs of the imported data
Will be used to generate files.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
import re

def build_list_thermos(list_tuple):
    """
    Input: list of tuple (time, rain)
    Output: list of rain
    """
    ret = [temp for (time, temp, rain, humidity) in list_tuple]
    # Open-Meteo API typically provides temperature_2m in Celsius.
    # If it were Kelvin, this conversion would be needed:
    # for i in ret:
    #     ret[ret.index(i)] = float(i) - 273.15
    return ret

def build_list_time(list_tuple):
    """
    Input: list of tuple (time, rain)
    Output: list of time
    """
    ret = [time for (time, temp, rain, humidity) in list_tuple]
    # Makes the date more readable
    for i in ret:
        # Assuming date format like 'YYYY-MM-DDTHH:MM'
        # Slicing to get 'MM-DD HHh'
        ret[ret.index(i)] = i[5:10] + " " + i[11:13] + "h"
    return ret

def build_rain_graph(dataframe: pd.DataFrame):
    """
    Builds a graph from a Pandas DataFrame.
    The DataFrame should have 'date' and 'temperature_2m' columns.
    """
    # Extract temperature data (assuming it's already in Celsius)
    list_thermos = dataframe['temperature_2m'].tolist()

    # Extract and format time data
    # Assuming 'date' column contains datetime objects or strings like 'YYYY-MM-DDTHH:MM'
    if pd.api.types.is_datetime64_any_dtype(dataframe['date']):
        list_time = dataframe['date'].dt.strftime('%m-%d %Hh').tolist()
    else: # Assuming string format
        list_time = [d[5:10] + " " + d[11:13] + "h" for d in dataframe['date']]

    plt.plot(list_time, list_thermos)

    # Put the X axis caption vertially
    plt.xticks(rotation=90, horizontalalignment='center', fontsize=4)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature in Paris over the next week")
    plt.grid(True)
    plt.savefig('weather_graph.png') # Save the graph to a file
    return 0

