import newspaper
import time
from newspaper import ArticleException
import json


class Article():
    page = ""
    content = ""
    keywords = []
    url = ""
    title = ""
    __article = None

    def __init__(self, url, title, *args, **kwargs):
        self.__article = newspaper.Article(url)
        self.url = url
        self.title = title
        self.content = kwargs.get('content', None)
        self.keywords = kwargs.get('keywords', None)

    def process(self):
        print("Processing {}".format(self.url))
        try:
            self.__article.download()

            self.__article.parse()
            self.__article.nlp()
        except:
            print("Failed to do things with {}".format(self.url))
            return False

        self.content = self.__article.text
        self.keywords = self.__article.keywords
        return True

    def get_keywords(self):
        if len(self.keywords) is 0:
            self.process()
        return self.keywords

    def __str__(self):
        return "Title: {}\nURL: {}\nContent: {}\nKeywords: {}".format(self.title, self.url, self.content, self.keywords)
    """
    returns an object this structure: 
    {
        "title": "the title of the article",
        "url": "URL of the article",
        ("scraped_at": "DD.MM.YYYY",) <= coming later 
        ("origin": "hackernoon.com")  <= coming later 
        "keywords": ["keyword1", "keyword2"]
        "content": "complete text content of the article which got extracted by newspaper"
    }
    """

    def to_beautiful_object(self):
        return {'title': self.title.replace("\n", ""), "url": self.url, "keywords": self.keywords, "content": self.content}
