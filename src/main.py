from jbzd import Scraper


scraper = Scraper()

# with open('page.txt', 'r', encoding='utf-8') as f:
#     page = f.read()

page = scraper.getPage(1)

articles = scraper.getArticles(page)

for article in articles:
    print(article)
