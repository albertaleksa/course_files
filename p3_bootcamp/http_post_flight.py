import requests
from requests.structures import CaseInsensitiveDict
import base64


def run():
    url = "https://flightaware.com/about/careers/position/12.C21/apply"
    payload = {
        'name': 'Albert Aleksa',
        'email': 'albert.aleksa.by@gmail.com'
    }
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {to_64()}"
    headers["Content-Type"] = "application/json"
    print(headers)
    response = requests.post(url, headers=headers, json=payload)

    print(response.status_code)
    print(response.text)
    print(response.json())


def to_64():
    sample_string = "Tier 2 Support Software Engineer (Flight Tracking)"
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string


if __name__ == "__main__":
       run()
