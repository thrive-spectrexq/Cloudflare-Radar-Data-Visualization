import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API token from the environment variable
API_TOKEN = os.getenv("RADAR_API_TOKEN")

if API_TOKEN is None:
    raise ValueError(
        "API token not found. Please set RADAR_API_TOKEN in the .env file."
    )


def fetch_data():
    url = "https://api.cloudflare.com/client/v4/radar/dns/top/locations?domain=google.com&dateRange=1d&format=json&limit=2"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None
