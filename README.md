# weather-bot-pm-study

This repository contains a Python script for visualizing PM2.5 data from PurpleAir.

## Description

The `pm25_visualization.py` script allows you to:

* Fetch historical PM2.5 data from PurpleAir for multiple locations.
* Visualize the data to observe trends and patterns.
* Analyze the impact of events like wildfires on air quality.

## Usage

1.  **Install dependencies:**

    ```bash
    pip install requests pandas
    ```

2.  **Obtain a PurpleAir API key:**

    *   Follow the instructions at [https://develop.purpleair.com/](https://develop.purpleair.com/)

3.  **Configure the script:**

    *   Edit the `weather.config.cfg` file to specify:
        *   Your PurpleAir API key.
        *   The locations you want to track (with latitude and longitude).
        *   The start and end dates for the data retrieval.

4.  **Run the script:**

    ```bash
    python pm25_visualization.py
    ```

    You can optionally specify a different config file:

    ```bash
    python pm25_visualization.py -c my_config.json.cfg
    ```

## Contributing

Feel free to contribute to this project by:

*   Adding more visualization features.
*   Improving the data analysis.
*   Expanding the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.