from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class ReadWriteScraper(SiteScraper):

    def scrape(self):
        page = requests.get("https://readwrite.com")
        soup = BeautifulSoup(page.text, features="lxml")
        headlines = [x.text for x in soup.find_all("h2", "entry-title")]
        links = [x.findChildren("a", recursive=False)[0]["href"]
                 for x in soup.findAll("h2", "entry-title")]
        self.__update_articles(list(zip(links, headlines)))
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
