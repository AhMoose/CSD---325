import requests
import json

# Test connection to the API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

print("Connection Test")
print("Status Code:", response.status_code)

print("\nRaw Response")
print(response.text)

print("\nFormatted Response")
data = response.json()

print("People currently in space:", data["number"])
print()

for person in data["people"]:
    print("Name:", person["name"])
    print("Craft:", person["craft"])
    print()