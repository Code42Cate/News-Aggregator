class SiteScraper():
    articles = []

    def __init__(self, loaded_articles=None):
        if(loaded_articles is not None):
            self.articles = loaded_articles

    def scrape(self):
        self.articles.append(("url", "title"))
        return self

    def get_articles(self):
        return self.articles

    def __close_session(self):
        pass
