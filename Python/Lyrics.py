import requests
import string
from bs4 import BeautifulSoup

class Lyrics:
    def __init__(self, artist, title):
        self.title = title
        self.artist = artist
        self.get_lyrics()

    def get_lyrics(self):
        URL = self.get_url()
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        lyrics = soup.findAll('div', attrs = {'class':'lyrics'})
        self.lyrics = lyrics[0].text

    def get_url(self):
        temp_title = self.title.translate(str.maketrans(' ', '-', string.punctuation))
        temp_artist = self.artist.translate(str.maketrans(' ', '-', string.punctuation))
        url = "https://www.genius.com/%s-%s-lyrics" % (temp_artist, temp_title)
        return url


things = Lyrics('Drake', '(Toosie Slide')
print(things.lyrics)
