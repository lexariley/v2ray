
import requests

def get_country_emoji(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        data = response.json()
        country_code = data.get("country", "").strip().upper()
        if country_code:
            return chr(0x1F1E6 + ord(country_code[0]) - 65) + chr(0x1F1E6 + ord(country_code[1]) - 65)
    except Exception:
        pass
    return "🌐"

# Sample test
if __name__ == "__main__":
    print(get_country_emoji("8.8.8.8"))  # Should print 🇺🇸
