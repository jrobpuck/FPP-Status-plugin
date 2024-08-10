import sys
import json
import requests

# Configuration
config_file = '/home/fpp/media/plugins/FPP-Status-plugin/config.ini'

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

# Read the input data from FPPD
input_data = sys.stdin.read()
try:
    data = json.loads(input_data)
    if data.get('type') == 'media':
        song_info = {
            'title': data.get('title', ''),
            'artist': data.get('artist', ''),
            'album': data.get('album', ''),
            'media': data.get('Media', '')
        }
        # Send the song information to your website
        response = requests.post(website_url, data=song_info)
        response.raise_for_status()
        print(f"Successfully updated song on website: {song_info}")
    else:
        print(f"Unhandled type: {data.get('type')}")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except requests.exceptions.RequestException as e:
    print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
