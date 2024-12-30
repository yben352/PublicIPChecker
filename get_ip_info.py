import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json()["ip"]
    except Exception as e:
        return f"Error: {e}"

def get_ip_info():
    try:
        ip = get_public_ip()
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        ip_data = response.json()
        location_info = {
            "IP": ip,
            "City": ip_data.get("city", "Not available"),
            "Region": ip_data.get("region", "Not available"),
            "Country": ip_data.get("country", "Not available"),
            "Location": ip_data.get("loc", "Not available")
        }
        return location_info
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    ip_info = get_ip_info()
    if isinstance(ip_info, dict):
        print("Your public IP address information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print(ip_info)
