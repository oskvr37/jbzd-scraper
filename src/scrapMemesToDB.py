import os
from jbzd import Scraper, Database

# get mongoDB connection string from
# os environment
DB_URI = os.environ['MongoDB']

# init database and scraper
database = Database(DB_URI)
scraper = Scraper()

# get first page of jbzd page
# this returns string with html content
page = scraper.getPage(1)

# scrap memes from the page
# returning list of articles (memes)
articles = scraper.getArticles(page)

# insert every article to the database
for article in articles:
    database.insertArticle(article)
