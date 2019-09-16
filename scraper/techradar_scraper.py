from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class TechRadarScraper(SiteScraper):

    def scrape(self):
        page = requests.get("https://www.techradar.com")
        soup = BeautifulSoup(page.text, features="lxml")
        headlines = [x["aria-label"]
                     for x in soup.find_all("a", "article-link")]
        links = [x["href"] for x in soup.find_all("a", "article-link")]
        self.__update_articles(list(zip(links, headlines)))
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()

