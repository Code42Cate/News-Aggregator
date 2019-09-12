from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class SlashDotScraper(SiteScraper):

    def scrape(self):
        page = requests.get("https://slashdot.org/")
        soup = BeautifulSoup(page.text, features="lxml")
        headlines = [x.text for x in soup.find_all("span", "story-title")]
        links = [x["href"] for x in soup.findAll("a", "story-sourcelnk")]
        self.__update_articles(list(zip(links, headlines)))
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()