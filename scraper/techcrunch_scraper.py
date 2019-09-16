from scraper import SiteScraper
import requests
from bs4 import BeautifulSoup


class TechCrunchScraper(SiteScraper):
    def scrape(self):
        try:
            r = requests.get("https://techcrunch.com/")
            soup = BeautifulSoup(r.text, features="lxml")
            headlines = [x.text.replace("\n", "").replace("\t", "")
                         for x in soup.find_all("a", "post-block__title__link")]
            links = [x["href"]
                     for x in soup.findAll("a", "post-block__title__link")]

            self.__update_articles(list(zip(links, headlines)))
        except Exception as e:
            print(str(e))
        return self

    # This should eventually already kill duplicates
    def __update_articles(self, articles):
        self.articles = articles

    def get_articles(self):
        return super().get_articles()
