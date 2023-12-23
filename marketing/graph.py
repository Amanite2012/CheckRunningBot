"""
File used to generate graphs of the imported data
Will be used to generate files.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

def build_list_thermos(list_tuple):
    """
    Input: list of tuple (time, rain)
    Output: list of rain
    """
    return [rain for (time, rain) in list_tuple]

def build_list_time(list_tuple):
    """
    Input: list of tuple (time, rain)
    Output: list of time
    """
    return [time for (time, rain) in list_tuple]

def build_rain_graph(list_tuple):
    list_thermos = build_list_thermos(list_tuple)
    list_time = build_list_time(list_tuple)
    plt.figure(figsize=(10, 6))
    plt.plot(list_time, list_thermos)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature in Paris over the past week")
    plt.grid(True)
    plt.show()
    return 0

