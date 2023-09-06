import random
from random import choice

import requests
from bs4 import BeautifulSoup

import lxml


def get_fresh_news():
    schema = 'http://www.patriarchia.ru/'
    response = requests.get('http://www.patriarchia.ru/db/news/')
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    fresh_news = [x.find('a')['href'] for x in soup.find_all('h4', class_="title")]
    link = random.choice(fresh_news)
    final_url = f'{schema}{link}'
    final_response = requests.get(final_url)
    final_soup = BeautifulSoup(final_response.text, 'lxml')
    text_news = final_soup.find('div', class_='text').text
    return text_news
