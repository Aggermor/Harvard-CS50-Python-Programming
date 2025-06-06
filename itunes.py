# `$ python itunes.py weezer` # This terminal command runs the script with "weezer" as the argument, which will search for songs by the artist Weezer on iTunes.
# `$ python itunes.py "Avenged Sevenfold"` this did not work because the sys.argv is not properly handled for multi-word artist names?
# 
# https://youtu.be/nLRL_NcnK-4?t=20700
# API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. 
#     --> It allows different software components to communicate with each other.
#
# https://pypi.org/projects/requests/
# 'requests' is a package that allows you to send HTTP requests in Python. 
#     --> You can use it like a web browser to interact with web services and APIs.
#
# JSON (JavaScript Object Notation) is a data format that is easy to read and write for humans and machines.
#     --> It is often used to exchange data between a server and a client in web applications. Or from different programming languages.

import requests     # https://pypi.org/project/requests/
import sys          # https://docs.python.org/3/library/sys.html
import json         # https://docs.python.org/3/library/json.html

if len(sys.argv) != 2:
    print("Usage: python itunes.py <artist_name>")
    sys.exit(1)

artist_name = sys.argv[1]
LIMIT = 5
url = f"https://itunes.apple.com/search?entity=song&limit={LIMIT}&term={artist_name}"

response = requests.get(url)
dumps = json.dumps(response.json(), indent=2)  # Format the JSON response for better readability

# print(f"Response:\n{dumps}") discover the response structure. 
# I found that the response is a dictionary with a 'results' key.
# 'results' is a list of dictionaries, each representing a song.
# each song dictionary contains keys like 'trackName', 'artistName', 'collectionName', and 'previewUrl'.

data = response.json() # store the JSON response in an object 'data'
results = data['results']  # Use .get() to avoid KeyError if 'results' is not present

i = 1 # Initialize a counter for track numbering
for result in results:
    trackName = result['trackName'] # return the value associated with the key 'trackName'
    print(f"{i}. Track: {trackName}")
    i += 1