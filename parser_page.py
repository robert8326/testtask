import requests
from bs4 import BeautifulSoup


def get_parse_data(urls: list):
    for url in urls:
        try:
            page = requests.get(url)
            title = BeautifulSoup(page.content, 'html.parser').title.text
        except Exception as e:
            title = str(e)
        yield {'url': title}
