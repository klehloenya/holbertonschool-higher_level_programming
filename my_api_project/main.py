import requests

# Example API URL
url = 'https://api.example.com/data'

# Example headers, replace with actual API token if needed
headers = {
    'Authorization': 'Bearer <your-token>',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
