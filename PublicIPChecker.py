import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json()["ip"]
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Your public IP address is :", get_public_ip())
