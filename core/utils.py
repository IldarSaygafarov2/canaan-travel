import time
import requests
from bs4 import BeautifulSoup
from os.path import basename
import json
from django.conf import settings


def get_soup(url):
    html = requests.get(url).text
    return BeautifulSoup(html, 'html.parser')


def get_tours(url):
    soup = get_soup(url)
    wrapper = soup.find('div', class_='show-objects-container')
    res = []
    for item in wrapper.find_all('div', class_='show-objects-item'):
        title = item.find('a', class_='show-objects-title').get_text(strip=True)
        print(title)
        link = item.find('a', class_='show-objects-title')['href']
        try:
            tour_soup = get_soup(link)
        except:
            tour_soup = get_soup(link)
        wrapper = tour_soup.find('div', class_='wprt-container')

        res.append({
            'title': title,
            'link': link,
            'data': str(wrapper)
        })
        time.sleep(5)
    return res


tashkent_tours = get_tours('https://canaan.travel/uzbekistan/samarkand')

with open('../temp-data/khiva.json', mode='w', encoding='utf-8') as file:
    json.dump(tashkent_tours, file, indent=4, ensure_ascii=False)


def get_hotels_last_page(url):
    soup = get_soup(url)
    wrap = soup.find('div', class_='show-hotels-pagination')
    pages = [i.get_text(strip=True) for i in wrap.find_all('a')][-1]
    return int(pages)


# https://canaan.travel/ru/uzbekistan/hotels

def get_hotels(url, page_num=1):
    res = []

    if page_num == 1:
        soup = get_soup(url)
    else:
        soup = get_soup(url + f'/page/{page_num}')

    wrap = soup.find('div', class_='show-hotels-container')
    for hotel in wrap.find_all('div', class_='show-hotels-item'):
        title = hotel.find('a', class_='show-hotels-title').get_text(strip=True)
        price = hotel.find('div', class_='show-hotels-cost').get_text(strip=True).split('/')[0]
        img = hotel.find('img')['data-src']

        res.append({
            'title': title,
            'price': price,
            'img': img
        })
        print(title)
    return res


# hotels = get_hotels('https://canaan.travel/ru/uzbekistan/hotels/page/21')
# with open('../temp-data/hotels-21.json', mode='w', encoding='utf-8') as file:
#     json.dump(hotels, file, indent=4, ensure_ascii=False)