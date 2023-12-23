"""
File used to generate graphs of the imported data
Will be used to generate files.
"""
import pandas as pd

def build_list_rain(list_tuple):
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
    list_rain = build_list_rain(list_tuple)
    list_time = build_list_time(list_tuple)
    return 0

