# https://youtu.be/nLRL_NcnK-4?t=20700
# API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. 
#     --> It allows different software components to communicate with each other.

# https://pypi.org/projects/requests/
# 'requests' is a package that allows you to send HTTP requests in Python. 
#     --> You can use it like a web browser to interact with web services and APIs.

# JSON (JavaScript Object Notation) is a data format that is easy to read and write for humans and machines.
#     --> It is often used to exchange data between a server and a client in web applications. Or from different programming languages.

import requests
import sys
import json # https://docs.python.org/3/library/json.html

def main():
    v1()

def v1():
    if len(sys.argv) != 2:
        print("Usage: python itunes.py <artist_name>")
        sys.exit(1)

    artist_name = sys.argv[1]
    LIMIT = 2
    url = f"https://itunes.apple.com/search?entity=song&limit={LIMIT}&term={artist_name}"
    
    response = requests.get(url)
    dumps = json.dumps(response.json(), indent=2)  # Format the JSON response for better readability
    
    # print(f"Response:\n{dumps}") discover the response structure. 
    # I found that the response is a dictionary with a 'results' key.
    # 'results' is a list of dictionaries, each representing a song.
    # each song dictionary contains keys like 'trackName', 'artistName', 'collectionName', and 'previewUrl'.
    
    o = response.json() # store the JSON response
    results = o.get('results', [])  # Use .get() to avoid KeyError if 'results' is not present
    
    for result in results:
        trackName = result['trackName'] # return the value associated with the key 'trackName'
        print(f"Track: {trackName}")

main()