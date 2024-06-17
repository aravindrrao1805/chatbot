import requests

# Define the URL and the payload
url = "http://127.0.0.1:8090/sum"
payload = {
    "a": 5,
    "b": 3
}

# Make the POST request
response = requests.post(url, json=payload)

# Handle the response
if response.status_code == 200:
    result = response.json()
    print(f"The sum of {payload['a']} and {payload['b']} is {result['sum']}")
else:
    print(f"Failed to get a response: {response.status_code}")


queryUrl = "http://127.0.0.1:8090/query"
queryPayload = {
    "question": "Why should we choose python over R?"
}

response = requests.post(queryUrl, json=queryPayload)
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Failed to get a response: {response.status_code}")
