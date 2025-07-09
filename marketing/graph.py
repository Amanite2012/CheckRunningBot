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
    # plt.show() # Commented out to prevent GUI display in non-interactive environments
    plt.savefig("temperature_graph.png") # Save the plot
    print("Temperature graph saved as temperature_graph.png")
    return 0


def generate_meteo_graph(df: pd.DataFrame, output_path: str = "meteo_graph.png"):
    """
    Generates a graph with temperature, humidity, rain, and cloud cover from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing 'date', 'temperature_2m',
                           'relative_humidity_2m', 'rain', and 'cloud_cover' columns.
        output_path (str): Path to save the generated graph image.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input 'df' must be a pandas DataFrame.")

    required_columns = ['date', 'temperature_2m', 'relative_humidity_2m', 'rain', 'cloud_cover']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame must contain column: {col}")

    fig, axs = plt.subplots(4, 1, figsize=(12, 16), sharex=True) # 4 rows, 1 column

    # Temperature
    axs[0].plot(df['date'], df['temperature_2m'], label='Temperature (°C)', color='red')
    axs[0].set_ylabel('Temperature (°C)')
    axs[0].set_title('Meteorological Data Over Time')
    axs[0].grid(True)
    axs[0].legend()

    # Relative Humidity
    axs[1].plot(df['date'], df['relative_humidity_2m'], label='Relative Humidity (%)', color='blue')
    axs[1].set_ylabel('Relative Humidity (%)')
    axs[1].grid(True)
    axs[1].legend()

    # Rain
    axs[2].plot(df['date'], df['rain'], label='Rain (mm)', color='green')
    axs[2].set_ylabel('Rain (mm)')
    axs[2].grid(True)
    axs[2].legend()

    # Cloud Cover
    axs[3].plot(df['date'], df['cloud_cover'], label='Cloud Cover (%)', color='gray')
    axs[3].set_ylabel('Cloud Cover (%)')
    axs[3].set_xlabel('Date/Time')
    axs[3].grid(True)
    axs[3].legend()

    plt.xticks(rotation=45)
    plt.tight_layout() # Adjust layout to prevent overlapping titles/labels

    try:
        plt.savefig(output_path)
        print(f"Graph saved to {output_path}")
    except Exception as e:
        print(f"Error saving graph: {e}")
        raise
    finally:
        plt.close(fig) # Close the figure to free memory
