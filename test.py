import requests

BASE = "http://127.0.0.1:5000/"

stringer = '1'


response = requests.put(BASE + "text/" + stringer, json={'text': 'Michael Fortanely is cool'})
print(response.json())
