from pymongo import MongoClient
from .article import Article


class Database:
    def __init__(self, uri, name='jbzd') -> None:
        self.client = MongoClient(uri)
        self.db = self.client[name]

    # create toDoc method to article

    def insertArticle(self, article: Article):
        # id duplicate exception may occur
        db_articles = self.db['articles']
        doc = {
            '_id': article._id,
            'title': article.title,
            'src': article.src,
            'type': article.type
        }
        db_articles.insert_one(doc)

    def insertArticles(self, articles: list[Article]):
        # id duplicate exception may occur
        db_articles = self.db['articles']
        docs = []
        for article in articles:
            doc = {
                '_id': article._id,
                'title': article.title,
                'src': article.src,
                'type': article.type
            }
            docs.append(doc)
        db_articles.insert_many(docs)
