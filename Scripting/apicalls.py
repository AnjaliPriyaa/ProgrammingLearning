import requests
url = "https://api.example.com/servers"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Request failed:", response.status_code)

except requests.RequestException as e:
    print("API error:", e)