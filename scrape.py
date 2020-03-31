import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(links,votes):
    hn = []
    for idx, item in enumerate(links):
        titel = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append({'titel': titel, 'link': href})
    return hn

print(create_custom_hn(links, votes))