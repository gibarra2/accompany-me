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

def process_response(response):
    '''
    Parses response object from forward geocoding request to LocationIQ. 
    Returns coordinates from JSON response. 
    '''
    response_body = response.json()
    coord = {}
    coord["lat"] = response_body[0]["lat"]
    coord["lng"] = response_body[0]["lon"]

    return coord

def city_geocoding(city, country): 
    '''
    Takes in city (str) and country (str). 
    Returns dict with latitude and longitude of that city. 
    '''
    query_params["q"] = f"${city}, ${country}"
    response = requests.get(path, params=query_params)

    return process_response(response)

def address_geocoding(address):
    '''
    Takes in a place's address (str). 
    Returns dict with latitude and longitude of that address.
    '''
    query_params["q"] = address
    response = requests.get(path, params=query_params)

    return process_response(response)