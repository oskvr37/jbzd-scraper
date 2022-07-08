from jbzd import Scraper


scraper = Scraper()

page = scraper.getPage(1)

articles = scraper.getArticles(page)

for article in articles:
    print(article)
