import requests
import threading

urls = [
    "https://www.google.com",
    "https://www.github.com",
    "https://tactics.tools/explorer",
    "https://www.youtube.com",
    "https://www.reddit.com",
    "https://bunnymuffins.lol"
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} är uppe!")
        else:
            print(f"{url} är nere! Statuskod: {response.status_code}")
    except requests.RequestException as e:
        print(f"{url} är nere! Fel: {e}")

threads = []
for url in urls:
    t = threading.Thread(target=check_website, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Kontroll av webbplatser är klar.")