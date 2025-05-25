# CheckRunningBot


## Docker Usage

This application can be built and run as a Docker container.

### Prerequisites

*   Docker installed on your system.
*   The following environment variables need to be set when running the container:
    *   `LATITUDE`: The latitude for the weather forecast (e.g., "48.8566").
    *   `LONGITUDE`: The longitude for the weather forecast (e.g., "2.3522").
    *   `DISCORD_WEBHOOK_URL`: The Discord webhook URL to send messages to.

### Building the Image

To build the Docker image, navigate to the root directory of the repository and run:

```sh
docker build -t weather-reporter .
```

### Running the Container

To run the Docker container, use the following command, replacing the placeholder values for the environment variables:

```sh
docker run --rm \
  -e LATITUDE="your_latitude" \
  -e LONGITUDE="your_longitude" \
  -e DISCORD_WEBHOOK_URL="your_discord_webhook_url" \
  weather-reporter
```

The application will execute `main.py`, fetch weather data, potentially generate a graph (`weather_graph.png` - this file will be inside the container), and send a message to the configured Discord webhook.

### Weekly Automation

This repository includes a GitHub Actions workflow (`.github/workflows/weekly_run.yml`) that automatically builds and runs this Docker container every Sunday at midnight UTC. The required environment variables for this automated run should be configured as secrets in the GitHub repository settings (`Settings > Secrets and variables > Actions`).
