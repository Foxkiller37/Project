import time
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 YaBrowser/20.2.1.234 Yowser/2.5 Yptp/1.56 Safari/537.36'}
base_url = 'https://yandex.ru/news/quotes/1501.html'

def med(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    if request.status_code == 200:
        start = time.time()
        soup = bs(request.content, 'lxml')
        divs = soup.find_all('div', attrs={'quote__data'})
        for div in divs:
            title = div.find('caption', attrs={'quote__data-title'}).text
            date = div.find('th', attrs={'quote__date'}).text
            quote = div.find('th', attrs={'quote__value'}).text
            change = div.find('th', attrs={'quote__change'}).text
            data = div.find('td', attrs={'quote__date'}).text
            znachenie = div.find('td', attrs={'quote__value'}).text
            raznica = div.find('td', attrs={'quote__change'}).text

        finish = time.time()
        result = finish - start
        print('lxml = ' + str(result))
        print(title, date, quote, change, data, znachenie, raznica)
    else:
        print(soup)
med(base_url, headers)
