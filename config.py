import os

# Configurations for the Website
GOOGLE_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
WIKI_SEARCH_URL = "https://fr.wikipedia.org/w/api.php"

# Define the API Key in your server config 
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")


