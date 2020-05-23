import bs4 as bs
from urllib.request import urlopen, Request

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
reg_url = "https://genius.com/Drake-toosie-slide-lyrics"
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
print(html)

#source = urllib.request.urlopen('https://genius.com/Drake-toosie-slide-lyrics').read()

#soup = bs.BeautifulSoup(source, 'lxml')

#print(soup.find_all('div.lyrics'))
