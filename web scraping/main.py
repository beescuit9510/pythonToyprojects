import requests
import bs4

res = requests.get('https://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(soup('.author'))

authors = set()
for name in soup.select('.author'):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)


c = soup.select('.col-md-4.tags-box')[0]
tags = []
for tag in c.select('.tag'):
    tags.append(tag.text)



authors = set()
url = 'https://quotes.toscrape.com/page/'
for n in range(1, 10):
    base_url = url+str(n)
    res = requests.get(base_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for unique in soup.select('.author'):
        authors.add(unique.text)



n = 0
authors = set()
url = 'https://quotes.toscrape.com/page/{}/'
valid_page = True
while valid_page:
    n += 1
    base_url = requests.get(url.format(n))
    soup = bs4.BeautifulSoup(base_url.text, 'lxml')
    if 'No quotes found!' in soup.text:
        break
    else:
        for unique in soup.select('.author'):
            authors.add(unique.text)


print(authors)