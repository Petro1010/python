import requests

response = requests.get("https://httpbin.org/delay/3", timeout=5)  #seeing if it satisfies the timeout limits

print(response.status_code)
