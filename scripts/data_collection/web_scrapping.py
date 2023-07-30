import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()


# Retrieve the url of the website to scrap.
# url = os.getenv("WEBSCRAPPING_URL")

def get_webscrapping_endpoint_data(base_api_url, endpoint=""):
    """
    Perform web scraping on a specified website endpoint and retrieve data.

    Args:
        base_api_url (str): The base URL of the website.
        endpoint (str, optional): The endpoint to access within the website. Defaults to an empty string.

    Returns:
        bs4.BeautifulSoup or None: The BeautifulSoup object containing the parsed HTML data if the request is successful,
        or None if the request fails.
    """
    data = None
    webscrapping_url = f"{base_api_url.rstrip('/')}/{endpoint.lstrip('/')}"

    response = requests.get(webscrapping_url)

    if response.status_code == 200:
        data = BeautifulSoup(response.content, "html.parser")
    else:
        print("Failed to retrieve data from the website.")

    return data
