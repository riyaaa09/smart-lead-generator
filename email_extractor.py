import requests
import re

def extract_email(url):
    try:
        response = requests.get(url, timeout=3)

        emails = re.findall(r"[\w\.-]+@[\w\.-]+", response.text)

        return emails[0] if emails else "Not Found"

    except:
        return "Error"