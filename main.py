import call_api.meteo as meteo
import marketing.graph as graph
import marketing.discord_ex as discord_ex
import dotenv
import os

def main():
    """
    Main function to fetch weather data, generate a graph, and send it to Discord.
    """
    # Load environment variables from .env file
    dotenv.load_dotenv()

    print("Fetching meteorological data...")
    dataframe = meteo.get_meteo_pd()

    if dataframe is not None and not dataframe.empty:
        graph_file_path = "meteo_conditions_graph.png"
        print(f"Generating graph: {graph_file_path}...")
        try:
            graph.generate_meteo_graph(dataframe, graph_file_path)

            message = "Hourly Meteorological Conditions Forecast. Graph includes Temperature, Humidity, Rain, and Cloud Cover."
            print("Sending graph to Discord...")
            discord_ex.send_image_to_discord(graph_file_path, message)

            # Clean up the generated graph file after sending
            try:
                os.remove(graph_file_path)
                print(f"Cleaned up temporary graph file: {graph_file_path}")
            except OSError as e:
                print(f"Error deleting graph file {graph_file_path}: {e}")

        except Exception as e:
            print(f"An error occurred during graph generation or sending: {e}")
    else:
        print("Failed to retrieve data or data is empty. Skipping graph generation and Discord message.")

if __name__ == "__main__":
    main()
