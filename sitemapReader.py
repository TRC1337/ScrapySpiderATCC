import requests
from bs4 import BeautifulSoup
import csv

sitemaps = ['https://www.atcc.org/sitemap/product_sitemap1.xml',
            'https://www.atcc.org/sitemap/product_sitemap2.xml',
            'https://www.atcc.org/sitemap/product_sitemap3.xml']

for url in sitemaps:
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'xml')
    links = sp.find_all('loc')

    with open('data/sitemap.csv', 'a', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for link in links:
            writer.writerow({link.text})
