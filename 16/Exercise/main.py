import requests

url = "https://api.thecatapi.com/v1/breeds"

response = requests.get(url)
print(response)
cats = response.json()
print(cats[:1])

