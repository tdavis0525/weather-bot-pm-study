import requests
import pandas as pd
import json
import argparse

# --- Constants ---
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key

# --- Functions ---

def get_pm25_data(lat, lon, start_date, end_date):
    url = "https://api.purpleair.com/v1/historical"
    params = {
        "fields": "pm2.5_atm",
        "location_type": "0",  # Outdoor sensor
        "start_timestamp": int(pd.to_datetime(start_date).timestamp()),
        "end_timestamp": int(pd.to_datetime(end_date).timestamp()),
        "lat": lat,
        "lon": lon,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data["data"], columns=data["fields"])
    df["time_stamp"] = pd.to_datetime(df[0], unit='s')
    return df

def visualize_pm25(locations, start_date, end_date):
    data = {}
    for location_name, (lat, lon) in locations.items():
        data[location_name] = get_pm25_data(lat, lon, start_date, end_date)

    # ... (add visualization code here - e.g., using matplotlib or Google Earth)

# --- Configuration ---

def load_config(config_file):
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Config file not found: {config_file}")
        return None

# --- Main ---

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize PM2.5 data from PurpleAir.")
    parser.add_argument("-c", "--config", help="Path to the config file (optional)")
    args = parser.parse_args()

    config_file = args.config if args.config else "weather.config"
    config = load_config(config_file)

    if config:
        locations = config.get("locations", {})
        start_date = config.get("start_date", "2023-07-01")
        end_date = config.get("end_date", "2023-08-31")

        visualize_pm25(locations, start_date, end_date)
    else:
        print("Exiting due to missing or invalid configuration.")