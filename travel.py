import requests
import json

r1 = requests.get("https://developer.citymapper.com/api/1/traveltime/?startcoord=51.525246%2C0.084672&endcoord=51.559098%2C0.074503&time=2014-11-06T19%3A00%3A02-0500&time_type=arrival&key=d4625ff00f826f01d0f9ea5cbc37d0dd")

r2 = requests.get("https://developer.citymapper.com/api/1/singlepointcoverage/?coord=51.578973%2C-0.124147&key=d4625ff00f826f01d0f9ea5cbc37d0dd")

print(r1.status_code)
print(r1.text)
print(r1.json())

print(r2.status_code)
print(r2.text)
print(r2.json())
