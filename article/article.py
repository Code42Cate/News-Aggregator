import newspaper
import time
from newspaper import ArticleException

class Article():
    page = ""
    content = ""
    keywords = []
    url = ""
    title = ""
    __article = None

    def __init__(self, url, title):
        self.__article = newspaper.Article(url)
        self.url = url
        self.title = title

    def process(self):
        print("Processing {}".format(self.url))
        try:
            self.__article.download()
        
            self.__article.parse()
            self.__article.nlp()
        except:
            print("Failed to do things with {}".format(self.url))
            pass
        self.content = self.__article.text
        self.keywords = self.__article.keywords

    def get_keywords(self):
        if len(self.keywords) is 0:
            self.process()
        return self.keywords
