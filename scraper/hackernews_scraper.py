from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class HackerNewsScraper(SiteScraper):

    def scrape(self):
        try:
            page = requests.get("https://thehackernews.com/")
            soup = BeautifulSoup(page.text, features="lxml")
            headlines = [x.text for x in soup.find_all("h2", "home-title")]
            links = [x["href"] for x in soup.findAll("a", "story-link")]
            self.__update_articles(list(zip(links, headlines)))
        except Exception as e:
            print(str(e))

        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
