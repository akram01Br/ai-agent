import requests

def search(topic):
    url = f"https://api.duckduckgo.com/?q={topic}&format=json"
    data = requests.get(url).json()
    return data.get("AbstractText", "No data found")