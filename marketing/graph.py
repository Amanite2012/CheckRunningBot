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
    for i in ret:
        ret[ret.index(i)] = float(i) - 273.15
    return ret

def build_list_time(list_tuple):
    """
    Input: list of tuple (time, rain)
    Output: list of time
    """
    ret = [time for (time, temp, rain, humidity) in list_tuple]
    # Makes the date more readable
    for i in ret:
        ret[ret.index(i)] = i[5:13] + "h"
    return ret

def build_rain_graph(list_tuple):
    list_thermos = build_list_thermos(list_tuple)
    list_time = build_list_time(list_tuple)
    plt.plot(list_time, list_thermos)

    # Put the X axis caption vertially
    plt.xticks(rotation=90, horizontalalignment='center', fontsize=4)
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature in Paris over the next week")
    plt.grid(True)
    plt.show()
    return 0

