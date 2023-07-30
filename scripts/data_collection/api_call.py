import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the API url and API key
# api_url = os.getenv("API_URL")
# api_key = os.getenv("API_KEY")

def get_api_endpoint_data(base_api_url, api_key=None, endpoint=""):
    """
    Make an HTTP GET request to the specified API endpoint and retrieve data.

    Args:
        base_api_url (str): The base URL of the API.
        api_key (str, optional): The API key to include in the request headers.
        endpoint (str, optional): The endpoint to access within the API.

    Returns:
        dict or None: The response data as a dictionary if the request is successful, or None if the request fails.
    """
    data = None
    headers = {}

    if api_key:
        headers['Authorization'] = f'Bearer {api_key}'

    api_url = f"{base_api_url.rstrip('/')}/{endpoint.lstrip('/')}"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Failed to retrieve data from the API.")

    return data
