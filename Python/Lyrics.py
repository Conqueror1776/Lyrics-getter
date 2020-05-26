import requests
from bs4 import BeautifulSoup

class Lyrics:
    lyrics = ''

    def get_lyrics(self):
        URL = "https://www.genius.com/Drake-toosie-slide-lyrics"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        lyrics = soup.findAll('div', attrs = {'class':'lyrics'})
        print(lyrics[0].text)

thigs = Lyrics()
thigs.get_lyrics()

"""
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
reg_url = "https://www.genius.com/Drake-toosie-slide-lyrics"
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
print(html)

with urlopen("https://www.genius.com/Drake-toosie-slide-lyrics") as response:
    html = response.read()
html = BeautifulSoup("https://genius.com/Drake-toosie-slide-lyrics","html.parser")
div = html.find("div", class_="lyrics")

#source = urllib.request.urlopen('https://genius.com/Drake-toosie-slide-lyrics').read()

#soup = bs.BeautifulSoup(source, 'lxml')

#print(soup.find_all('div.lyrics'))
"""
