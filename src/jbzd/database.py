from pymongo import MongoClient
from .article import Article


class Database:
    def __init__(self, uri, name='jbzd') -> None:
        self.client = MongoClient(uri)
        self.db = self.client[name]

    def insertArticle(self, article: Article):
        articles = self.db['articles']
        doc = {
            '_id': article._id,
            'title': article.title,
            'src': article.src,
            'type': article.type
        }
        articles.insert_one(doc)
