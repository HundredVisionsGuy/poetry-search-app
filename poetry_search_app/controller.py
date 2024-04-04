"""controller.py
by Chris Winikka
Various functions for dealing with API calls and
data functionality.
"""

# imports
import requests as re


def get_api_data(endpoint: str, query=""):
    domain = "https://poetrydb.org/"
    if query:
        url = domain + endpoint + "/" + query
    else:
        url = domain + endpoint
    response = re.get(url)

    if response.ok:
        results = response.text
    else:
        results = "Error!"
    return results


if __name__ == "__main__":
    call = get_api_data("author", "shakespeare")
    print(call)
    call = get_api_data("title")
    print(call)
