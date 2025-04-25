import requests
import threading
import random
import os
from dotenv import load_dotenv
import json

load_dotenv()

proxy_url = os.environ.get('PROXY_URL', None)

proxies = {
    "http": proxy_url,
    "https": proxy_url
}
proxies = proxies if proxy_url else None

count = 0
counter_lock = threading.Lock()

url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSd3otniyGl35qcAXKI2bLRAoUNCfaUBiqHeru5m7y4BXNipyw/formResponse"

# Inspect Network tab and find find post request to get payload data
# print(os.environ.get('FORM_PAYLOAD'))
# payload = json.loads(os.environ.get('FORM_PAYLOAD').replace("\\\\", "\\"))
payload = {"entry.1969450330":"House TAU"}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}

def submit_form():
    global count
    
    while True:
        try:
            response = requests.post(url, data=payload, headers=headers, proxies=proxies, timeout=10)

            if response.status_code == 200:
                with counter_lock:
                    count += 1
            print(f"Response: {response.status_code} | Count: {count}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

def main():
    threads = []
    num_threads = 5  # Adjust based on available proxies
    
    for _ in range(num_threads):
        thread = threading.Thread(target=submit_form)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
