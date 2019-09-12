from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class DiggScraper(SiteScraper):

    def scrape(self):
        page = requests.get("https://digg.com/channel/technology")
        soup = BeautifulSoup(page.text, features="lxml")
        headlines = [x.text for x in soup.find_all("h2", "headline")]
        links = [x.parent["href"] for x in soup.findAll("h2", "headline")]
        self.__update_articles(list(zip(links, headlines)))
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()

