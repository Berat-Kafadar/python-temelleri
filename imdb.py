import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=hm_nv_menu"

headers = {
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find("ul", {"class":"ipc-metadata-list"}).find_all("li", limit = 100)
for item in liste:
  filmadi = item.find("h3", {"class":"ipc-title__text"}).text
  puan = item.find("span", {"class":"ipc-rating-star"}).text
  print(puan,filmadi)