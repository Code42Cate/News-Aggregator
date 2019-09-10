from scraper import SiteScraper
from bs4 import BeautifulSoup
import requests


class HackerNoonScraper(SiteScraper):
    def scrape(self):
        hackernoon_urls = ["https://hackernoon.com/tagged/cryptocurrency", "https://hackernoon.com/tagged/coding",
                           "https://hackernoon.com/tagged/artificial-intelligence", "https://hackernoon.com/tagged/futurism", "https://hackernoon.com/tagged/startups"]
        for hackernoon_topic_url in hackernoon_urls:
            page = requests.get(hackernoon_topic_url)
            soup = BeautifulSoup(page.text, features="lxml")
            titles = soup.find_all("div", "title")
            articles = []
            for title in titles:
                articles.append(("https://hackernoon.com" +
                                 title.findChildren("a", recursive=False)[0]["href"], title.text))
        self.__update_articles(articles)
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
