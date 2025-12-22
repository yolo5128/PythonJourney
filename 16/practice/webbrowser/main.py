import webbrowser
import requests

# get(): open a network to fetch data from url
# status_code: After data is fetched, checks status of operation
# headers: check the header types
# text: to extract text from the fetched response object
# json: to extract json data


url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)


print(response)
print(response.status_code)
countries = response.json
print(countries[:1])
# print(response.headers)
# print(response.text)