import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
url="https://www.harvard.edu/"
response = requests.get(url)
html=response.text
soup = BeautifulSoup(html, "html.parser")
links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])
b_links = []
base_url = "https://www.harvard.edu/"
data = {}
for jj in links:
    try:
        full_url = urljoin(base_url, jj)
        response1 = requests.get(full_url)
        html1=response1.text
        soup1 = BeautifulSoup(html1, "html.parser")
        text = soup1.get_text(separator="\n", strip=True)
        data[full_url] = text
    except Exception as e:
        print(f"❌ Error fetching {jj}: {e}")
        b_links.append(jj)
for url,text in data.items():
    print(f"URL:{url}\n")
    print(text)
for ii in b_links:
    print("These links diidnot work",ii)
        



