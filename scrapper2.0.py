import requests
from bs4 import BeautifulSoup

with open("C:/Users/Talal/Desktop/urls.txt", "r") as file:
    urls = file.read().splitlines()

cleaned_data = []

for url in urls:
    url = url.strip()
    if not url:
        continue
    print(f"Scraping: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["nav", "header", "footer", "script", "style", "noscript", "svg", "form"]):
            tag.decompose()


        main = soup.find("main") or soup 
        text_elements = main.find_all(["p", "h1", "h2", "h3", "li"])
        content = "\n".join([t.get_text(strip=True) for t in text_elements if t.get_text(strip=True)])

        cleaned_data.append({"url": url, "text": content})

    except Exception as err:
        print(f"❌ Failed: {url} | Error: {err}")

# Save all cleaned text into one file
with open("harvard_cleaned.txt", "w", encoding="utf-8") as f:
    for item in cleaned_data:
        f.write(f"URL: {item['url']}\n")
        f.write(item["text"] + "\n\n")
