import requests
import os

# Path to the config file
config_file = "/home/fpp/media/plugins/<YourPluginName>/config.ini"

# Load the website URL from the config file
website_url = ""
if os.path.exists(config_file):
    with open(config_file, 'r') as file:
        for line in file:
            if line.startswith("website_url="):
                website_url = line.strip().split('=', 1)[1]

if not website_url:
    print("Website URL not configured.")
    exit()

# FPP API URL to fetch the currently playing song
fpp_api_url = "http://<fpp_ip_address>/api/fppd/status"

try:
    # Fetch the FPPD status from the FPP API
    response = requests.get(fpp_api_url)
    response.raise_for_status()
    
    # Parse the JSON response
    status_data = response.json()

    # Extract the now playing information
    current_song = status_data.get('current_song', '')

    # Alternative keys if 'current_song' doesn't exist
    current_song_info = status_data.get('status', {}).get('current_song', '')
    media_file = status_data.get('mediaFilename', '')

    # Decide which data to use
    song_info = current_song_info or media_file or "No song playing"

    # Prepare the payload to send to your website
    payload = {'song': song_info}

    # Send the song information to your website
    response = requests.post(website_url, data=payload)
    response.raise_for_status()

    # Log the success
    print(f"Successfully updated song on website: {song_info}")

except requests.exceptions.RequestException as e:
    # Handle any HTTP errors or connection issues
    print(f"HTTP error occurred: {e}")
except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")
