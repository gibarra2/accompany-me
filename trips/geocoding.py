from dotenv import load_dotenv
import requests
import os

load_dotenv()

path = "https://us1.locationiq.com/v1/search"
key = os.environ.get("LOCATIONIQ_API_KEY")

query_params = {
    "key": key, 
    "q": "", 
    "format": "json"
}

def city_geocoding(city, country): 
    query_params["q"] = f"${city}, ${country}"
    response = requests.get(path, params=query_params)
    response_body = response.json()
    coord = {}
    coord["lat"] = response_body[0]["lat"]
    coord["lng"] = response_body[0]["lon"]

    return coord
