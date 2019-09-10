from scraper import SiteScraper
from bs4 import BeautifulSoup
import requests


class xkcdScraper(SiteScraper):
    def scrape(self):
        list = []
        r = requests.get("https://xkcd.com")
        soup = BeautifulSoup(r.text, features="lxml")
        list.append((soup.find("meta",  property="og:url")
                     ["content"], "Daily XKCD"))
        self.__update_articles(list)
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
