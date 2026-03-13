import requests

current_version = "1.0"

url = "http://localhost:8080/api/update/check"

try:
    response = requests.get(url, params={"version": current_version})
    data = response.json()

    if data["update"]:
        print("Update available")
        print("Latest version:", data["version"])
        print("Download URL:", data["url"])
    else:
        print("Already up to date")

except Exception as e:
    print("Failed to connect to update server:", e)