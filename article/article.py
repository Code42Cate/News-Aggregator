import newspaper
import time

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
        if newspaper.Article.is_valid_url(self.__article) is False:
            print("{} is invalid".format(self.url))
            return
        try:
            self.__article.download()
        except Exception as e:
            time.sleep(7)
            self.process()
            return
        self.__article.parse()
        self.__article.nlp()

        self.content = self.__article.text
        self.keywords = self.__article.keywords

    def get_keywords(self):
        if len(self.keywords) is 0:
            self.process()
        return self.keywords   
