import requests as r
from bs4 import BeautifulSoup

from .article import Article


class Scraper:
    def __init__(self) -> None:
        pass

    def getPage(self, page_number: int) -> str:
        url = f'https://jbzd.com.pl/str/{page_number}'

        request = r.get(url)

        if request.status_code == 200:
            return request.text
        else:
            return ''

    def getArticles(self, page: str) -> list[Article]:
        soup = BeautifulSoup(page, 'html.parser')
        articles = [Article(el) for el in soup.find_all('article')]
        return articles
